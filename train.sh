opencv_createsamples -img watch5050.jpg -bg  bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1165
opencv_createsamples  -info info/info.lst -num 1165 -w 20 -h 20 -vec positive.vec
opencv_traincascade -data data -vec positive.vec -bg bg.txt -numPos 1000 -numNeg 500 -numStages 5 -w 20 -h 20
