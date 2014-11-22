# -*- coding: utf-8 -*-
from __future__ import division
from flask import Flask, request, make_response, jsonify
from PIL import Image, ImageFilter
from io import BytesIO

import requests
import tempfile

app = Flask(__name__)


def semiflatten(multi):
    """Convert a MutiDict into a regular dict. If there are more than one value
    for a key, the result will have a list of values for the key. Otherwise it
    will have the plain value."""
    if multi:
        result = multi.to_dict(flat=False)
        for k, v in result.items():
            if len(v) == 1:
                result[k] = v[0]
        return result
    else:
        return multi


def renderImage():
    """
    This function looks at the url arguments from the request object and uses
    them as paramters to PIL.  It also creates the response object and sets
    the the correct http headers for the response.
    """
    args = semiflatten(request.args)
    r = requests.get(args['url'])
    image_temp = tempfile.NamedTemporaryFile(mode='w+b')
    i = Image.open(BytesIO(r.content))

    if args.get('crop'):
        rectCrop = map(int, args.get('crop').split(','))
        i = i.crop(tuple(rectCrop))

    if args.get('scale'):
        scaleVars = map(str, args.get('scale').split(','))
        orig_width = i.size[0]
        orig_height = i.size[1]
        if scaleVars[0] == '%':
            new_width = int(round(orig_width*float(scaleVars[1])))
            new_height = int(round(orig_height*float(scaleVars[1])))
            scaleSize = tuple([new_width, new_height])
        elif scaleVars[0] == 'width':
            ratio = int(scaleVars[1])/orig_width
            new_width = int(scaleVars[1])
            new_height = int(orig_height*ratio)
            scaleSize = tuple([new_width, new_height])
        elif scaleVars[0] == 'height':
            ratio = int(scaleVars[1])/orig_height
            new_width = int(orig_width*ratio)
            new_Height = int(scaleVars[1])
            scaleSize = tuple([new_width, new_Height])
        i = i.resize(scaleSize)

    if args.get('size'):
        size = tuple(map(int, args.get('size').split(',')))
        i = i.resize(size)

    if args.get('transpose'):
        transposeList = map(str, args.get('transpose').split(','))
        for x in xrange(0, len(transposeList)):
            if transposeList[x] == '90':
                action = Image.ROTATE_90

            elif transposeList[x] == '180':
                action = Image.ROTATE_180

            elif transposeList[x] == '270':
                action = Image.ROTATE_270

            elif transposeList[x] == 'top_bottom':
                action = Image.FLIP_TOP_BOTTOM

            elif transposeList[x] == 'left_right':
                action = Image.FLIP_LEFT_RIGHT

            i = i.transpose(action)

    if args.get('rotate'):
        i = i.rotate(int(args.get('rotate')))

    if args.get('blur'):
        i = i.filter(ImageFilter.GaussianBlur(radius=int(args.get('blur'))))

    i.save(image_temp, format='png')
    i.close()
    resp = make_response(open(image_temp.name).read())
    resp.headers['Content-Type'] = 'image/png'
    resp.headers['Cache-Control'] = 'public, max-age=3600'
    return resp


@app.route('/images/', methods=['GET'])
def images_route():
    """retutns the modified image"""
    return renderImage()


@app.route('/', methods=['GET'])
def get_args():
    """
    This function generates a json object containig information about the url
    paramters.
    """
    args = semiflatten(request.args)
    return jsonify(args)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5280)
