Image Magician

Description:

Image Magician is a utility for content manager that allows for easy image manipulation via a RESTful api.  Supported functions are resizing, cropping, rotating, transposing, and bluring.

Usage:

http://yourserver.com:5280/images
This is the main end point for image manipualtion
?url=http://example.com/image.png
please avoid urls with ampersands in them for now
?crop=upperLeftX,upperLeftY,LowerRightX,LowerRightY
this api considers the upper left of the image 0,0
?size=width,height
?transpose=action1,action2,action3,...
90, 180, 270, left\_right, top_bottom are options for actions.
90 , 180, and 270 transpose the image that many degrees.
left_right and top\_bottom flip across the y and x axes's respectively.
you can chain actions together so
?transpose=90,180,left_right would transpose the image 90 degrees, then 180 degrees, then flip it across the y axis
?rotate=angle
angle is counter clockwise

http://yourserver.com:5280/args
Returns a json response that contains the url paramters you passed.  You can easily switch from /images to /args to see what paramters you passed in the test window.
