Image Magician
==============
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/mikexocon/image-magician/tree/master)

## Description:


Image Magician is a utility for content manager that allows for easy image manipulation via a RESTful api.  Supported functions are resizing, cropping, rotating, transposing, and bluring.

## Usage:


-[`/images?url=value`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg) url of image

-[`/images?crop=upperLeftX,upperLeftY,LowerRightX,LowerRightY`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&crop=100,100,200,200) crops image

-[`/images?size=width,height`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&size=400,400) resizes image

-[`/images?transpose=action1,action2,action3,...`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&transpose=90,left_right) transposes image

-[`/images?rotate=angle`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&rotate=45) rotates the image

-[`/images?blur=radius`](http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&blur=4) Guaisian Blur

-[`/images/args`](http://imagemagician.mikexweb.com/images/args/?url=http://i.imgur.com/1GuBy9L.jpg) returns get parameters

## Examples

http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&crop=100,100,200,200&size=200,200

```This crops the image from http://i.imgur.com/1GuBy9L.jpg using the bounding box 100,100,200,200 and then resizes the cropped portion to 200x200 pixels```

http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&blur=4&rotate=45

```This will rotate the image from http://i.imgur.com/1GuBy9L.jpg and then do a guasian blur using a radius of 4.```

http://imagemagician.mikexweb.com/images/?url=http://i.imgur.com/1GuBy9L.jpg&transpose=90,left_right

```This will transpose the image from http://i.imgur.com/1GuBy9L.jpg and transpose it 90 degrees counter clockwise, and then flip it across the Y axis.```

## Notes
The order of operations is crop, resize, transpose, rotate, and then blur.  You can use any combination of paramters together to get the your intended effect.  You can also daisy chain transpose actions one after another by making them a comma seperated list and passing it through the query string.
