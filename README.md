# Foundation_of_Algo_Prog 01 -- Find m closeset points pairs.
## User Guide
### Using Packages:
```
math
random
argparse
```
Before Running the Code you should check if these packages are installed.

### How to use the code?

This program can run on the terminal with two required inputs: file path and number of closest points pairs.

``` python3 main.py --file_path ./template_input.txt --num 4``` 

And the result should present like:

```[[x_1, y_1], [x_2, y_2]] Distance: dist(pairnode)```

### Input file Requirement

If you want to use you own points data, please paste them into txt file, with each line containing only x and y coordinates like:
``` 
2 4
3 8
5 7
```
The first number is x value of the point, and the second would be y.

But if you want to create auto-randomized points set, you can use ***auto*** argument on the program, for example:
```
python3 Find_m_closest.py --file_path filename --num 4 --auto
```
--auto argument would wirte 100 randomized points into the file at provided file path. And the result is based on the randomized point sets.
you can see the its usage by running ``` python3 Find_m_closest.py -h ```
