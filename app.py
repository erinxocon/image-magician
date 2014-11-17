# -*- coding: utf-8 -*-

import requests
import tempfile

from flask import Flask, request, make_response, jsonify
from PIL import Image, ImageFilter
from io import BytesIO


app = Flask(__name__)


def renderImage():
    url = request.args.get('url', '')
    size = request.args.get('size', '')
    crop = request.args.get('crop', '')
    rotate = request.args.get('rotate', '')
    transpose = request.args.get('transpose', '')
    blur = request.args.get('blur', '')
    scale = request.args.get('scale', '')
    r = requests.get(url)
    image_temp = tempfile.NamedTemporaryFile(mode='w+b')
    i = Image.open(BytesIO(r.content))

    if crop:
        rectCrop = map(int, crop.split(','))
        i = i.crop(tuple(rectCrop))
    if scale:
        scaleVars = map(str, scale.split(','))
        orig_width = i.size[0]
        orig_height = i.size[1]
        if scaleVars[0] == '%':
            new_width = int(round(orig_width*float(scaleVars[1])))
            new_height = int(round(orig_height*float(scaleVars[1])))
            scaleSize = tuple([new_width, new_height])
        elif scaleVars[0] == 'width':
            ratio = int(scaleVars[1])/orig_width
            new_width = orig_width*ratio
            new_height = orig_height*ratio
            scaleSize = tuple([new_width, new_height])
        elif scaleVars[0] == 'height':
            ratio = int(scaleVars[1])/orig_height
            new_width = orig_width*ratio
            new_Height = orig_height*ratio
            scaleSize = tuple([new_width, new_Height])
        #i = i.resize(scaleSize)
    if size:
        size = tuple(map(int, size.split(',')))
        i = i.resize(size)

    if transpose:
        transposeList = map(str, transpose.split(','))
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

    if rotate:
        i = i.rotate(int(rotate))

    if blur:
        i = i.filter(ImageFilter.GaussianBlur(radius=int(blur)))

    i.save(image_temp, format='png')
    i.close()
    resp = make_response(open(image_temp.name).read())
    resp.headers['Content-Type'] = 'image/png'
    return str(1125/2250)


@app.route('/images/', methods=['GET'])
def images_route():

    return renderImage()


@app.route('/images/args/', methods=['GET'])
def get_args():
    url = request.args.get('url', '')
    size = request.args.get('size', '')
    crop = request.args.get('crop', '')
    rotate = request.args.get('rotate', '')
    transpose = request.args.get('transpose', '')
    blur = request.args.get('blur', '')
    scale = request.args.get('scale', '')
    return jsonify({'url': url, 'size': size, 'crop': crop, 'rotate': rotate, 'transpose': transpose, 'blur': blur, 'scale': scale})

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5280)
