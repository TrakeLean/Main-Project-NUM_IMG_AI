# Project Title

Simple overview of use/purpose.

## Description

An AI that's able to recognize the digits from 0 to 9. through your webcam. It's based on the MNIST dataset. It's a simple neural network with 1 hidden layers. It has 784 neurons. The activation function is ReLU. The optimizer is Adam. The loss function is categorical crossentropy. The accuracy is 98%.

## Getting Started

### Dependencies

*opencv-contrib-python 
*numpy
*tensorflow
*tensorflow_datasets
*imutils

### Installing

* gh repo clone TrakeLean/Main-Project-NUM_IMG_AI

### Executing program

There are two configurations when running the program. One is able to recognize more than two digits at the same time, but it has a major bug. The other one can only do two.

in cell 27 is where you choose between these two configurations.
```
temp_window = crop_shape(temp_window, zoom_ratio, 0, centercoords)
```
and 
```
temp_window = zoom_at(temp_window, zoom_ratio, 0, centercoords)
```


## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

[@TrakeLean](https://github.com/TrakeLean)
[@Snusemumrikken](https://github.com/Snusemumrikken)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)