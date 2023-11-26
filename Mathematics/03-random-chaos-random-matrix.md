## How to make a random position on chaos
Did you know about the matrix and fractal?\
Basic example of sierpinski:
```c
void sierpinski_arrowhead_curve(unsigned order, double length)
{
    // If order is even we can just draw the curve.
    if ( 0 == (order & 1) ) {
        curve(order, length, +60);
    }
    else /* order is odd */ {
        turn( +60);
        curve(order, length, -60);
    }
}
void curve(unsigned order, double length, int angle)
{
    if ( 0 == order ) {
        draw_line(length);
    } else {
        curve(order - 1, length / 2, -angle);
        turn(angle);
        curve(order - 1, length / 2, angle);
        turn(angle);
        curve(order - 1, length / 2, -angle);
    }
}
// credit for sierpinski code: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve
```
in this example we draw a "sierpinski" fractal by simple equation.\
imagin the "dot's" without the lines. before that you drawing this shape(dot's) on a page and have coordination of all point.\
Each point have a (x, y) as position, and on that position you have a unique "prime number".\
Now you can choose two random position and times that two numbers for generating a unique RSA...\
for more information read [this](https://github.com/mosi-arch/documents/blob/main/prime-number-cryptography.md) and [this](https://github.com/mosi-arch/documents/blob/main/safe-unique-random-number.md)

This equation make 2-dimensional shape on plate. in some cases we use sequence of fibonacci (golden ratio), but that equation have a problem: n+1/2n^2 . wasting time!\
So we use the fractal equations and fix time problem for creating randomness.\
in some cases we create our shape and move the plate of prime numbers for generating randomness method.\
for example: [this fingerprint indexing system](https://github.com/f-fq-academic/finger-print-revelution-studio/tree/master) you need just add a created {[Moore](https://en.wikipedia.org/wiki/Moore_curve)} fractal and use that on "minutia" for search equation on database. the answer is true+id or false, because "ALWAYS" we find true fingerprint. actually we moving the plate of fractal on fingerprints...

### note
The fractal each times create from random point of the "plate", so each time unique random series drawing.
