code_1 = """
/*
@title: getting_started
@tags: ['beginner', 'tutorial']
@img: ""
@addedOn: 2022-07-26
@author: leo, edits: samliu, belle, kara

Check the tutorial in the bottom right, the run button is in the top right.
Make sure to remix this tutorial if you want to save your progress!
*/

// define the sprites in our game
const player = "p";
const box = "b";
const goal = "g";
const wall = "w";


// assign bitmap art to each sprite
setLegend =
  [ player, bitmap`
................
................
................
.......0........
.....00.000.....
....0.....00....
....0.0.0..0....
....0......0....
....0......0....
....00....0.....
......00000.....
......0...0.....
....000...000...
................
................
................`],
  [ box, bitmap`
................
................
................
...88888888888..
...8....8....8..
...8....8....8..
...8....8....8..
...8....8....8..
...88888888888..
...8....8....8..
...8....8....8..
...8....8....8..
...8....8....8..
...88888888888..
................
................`],
  [ goal, bitmap`
................
................
................
....444444......
...44....44.....
...4......4.....
...4.......4....
...4.......4....
...4.......4....
...44......4....
....4......4....
....44....44....
.....444444.....
................
................
................`],
  [ wall, bitmap`
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000`]
);

// create game levels
let level = 0; // this tracks the level we are on
const levels = [
  map`
..p.
.b.g
....`,
  map`
p..
.b.
..g`,
  map`
p.wg
.bw.
..w.
..w.`,
  map`
p...
...b
...b
.bbg`,
  map`
...
.p.
...`,
  map`
p.w.
.bwg
....
..bg`
];

// set the map displayed to the current level
const currentLevel = levels[level];
setMap(currentLevel);

setSolids([ player, box, wall ]); // other sprites cannot go inside of these sprites

// allow certain sprites to push certain other sprites
setPushables({
  [player]: []
});

// inputs for player movement control
onInput("s", () => {
  getFirst(player).y += 1; // positive y is downwards
});

onInput("d", () => {
  getFirst(player).x += 1;
});

// input to reset level
onInput("j", () => {
  const currentLevel = levels[level]; // get the original map of the level

  // make sure the level exists before we load it
  if (currentLevel !== undefined) {
    clearText("");
    setMap(currentLevel);
  }
});

// these get run after every input
afterInput(() => {
  // count the number of tiles with goals
  const targetNumber = tilesWith(goal).length;
  
  // count the number of tiles with goals and boxes
  const numberCovered = tilesWith(goal, box).length;

  // if the number of goals is the same as the number of goals covered
  // all goals are covered and we can go to the next level
  if (numberCovered === targetNumber) {
    // increase the current level number
    level = level + 1;

    const currentLevel = levels[level];

    // make sure the level exists and if so set the map
    // otherwise, we have finished the last level, there is no level
    // after the last level
    if (currentLevel !== undefined) {
      setMap(currentLevel);
    } else {
      addText("you win!", { y: 4, color: color`3` });
    }
  }
});
"""
errors_1 = '[{"description":"SyntaxError: Unexpected token )\n    at <game>:89:1","raw":{"index":1622,"lineNumber":90,"description":"Unexpected token )"},"line":89,"column":1}]'


# Another code sample to try with 

code_2 = """
/*
First time? Check out the tutorial game:
https://sprig.hackclub.com/gallery/getting_started

@title: 
@author: 
@tags: []
@img: ""
@addedOn: 2024-00-00
*/

const player = "p"
const wheat = "w"
const seedling = "s"
const hoed_dirt = "h"

const dirt = "d"
const grass = "g"

setLegend(
  [ player, bitmap`
................
................
................
................
......66666.....
.....6666666....
...66666666666..
.....1111666....
....1101101.....
....11111111....
....11111111....
.....5L9L5......
....55999L55....
...55L292LL55...
....5L222L5L55..
..55L999999LL5..` ],a
  [ grass, bitmap`
................
................
................
................
................
................
................
................
................
................
................
................
.4..4.....4.....
..4.D4.4..D.4...
.4DD.D4.D.D4D.4.
DD4.DDDD4D4D.DD4` ],
  [ seedling, bitmap`
CCCCCCCCCCLCCCCC
C4FCCCCCFFFCLCC4
LD4FFFFF4FFF4FFD
FDDLCFC4DDCCDCDD
CDD4CCLDD4CCD4CC
CCCFLLFLFFFFDDFC
C4FFFFFFFFF4FFFC
FDDC4CCCCCC4CCCF
CD4CDD4CCCDDCCCC
CDDDD4DCC4DDDLCD
LFFDDDDFFFFFFFFL
FFFCCCCCCFFCFFFF
CCCD4CCCLCCCD4CD
DCL4DDFLFFF4DFFF
DFF4DD4FCF4DD4CC
FCDDDDDDCCDDDDDC` ],
  [ wheat, bitmap`
................
................
................
..6..F..........
..F..6..6....F..
..F..6.F6..F66.6
..6..F.F..6F.6.F
...6FF.6..F.6FF6
...6.6.F6.6.6F66
...6F6.F6.666F6.
.F66F66666F66.F6
..F66F6F66F.6.F.
.F66666F6F6666FF
.F66666.666..6F6
.6F6.F66666.666F
.666.F.6F.66F66F` ],
  [ dirt, bitmap`
  FFFFFFFFFFFFFFFC
  FFFFFFFFFFFFFFFF
  FFFFCFFFFFFFFFFF
  FFFCCCFFFFFFFFFF
  FFFCCFFFFFFFFFFF
  FFFFFFFFFFFFFFFF
  FFFFFFFFFFFFFFFF
  FFFFFFFFFCFFFFFF
  FFFFFFFFCCFFFFFF
  FFFFFFFFFFFFFFFF
  FFFFFFFFFFFFFFCF
  FFFFFFFFFFFFFCCF
  FFFFFFFFFFFFCFFF
  FFFFFFFFFFFFFFFF
  CFFFFFFFFFFFFFFF
  CCFFFFFFFFFFFFFF` ],
  [ hoed_dirt, bitmap`
CCCCCCCCCCLCCCCC
CLFCCCCCFFFCLCCF
LFFFFFFFFFFFFFFC
FCLLCFCCCCCCCCCC
CCCCCCLCCCCCCCCC
CCCFLLFLFFFFLCFC
CFFFFFFFFFFFFFFC
FFFCCCCCCCCCCCCF
CCCCCLCCCCCCCCCC
CLLCLFCCCCCCLLCC
LFFFFFFFFFFFFFFL
FFFCCCCCCFFCFFFF
CCCCCCCCLCCCCCCC
CCLFFCFLFFFFFFFF
CFFFFFFFCFCCFFCC
FCCCCCCCCCCCLCLC` ],
  
)

setSolids([])

setBackground(dirt);

let level = 0
const levels = [
  map`
p.
..`
]

setMap(levels[level])

setPushables({
  [ player ]: []
})

var plr_x = getFirst(player).x
var plr_y = getFirst(player).y


if (plr_x == 0) {
  level = level + 1;
  setMap(levels[level])
}

onInput("w", () => {
  getFirst(player).y -= 1
  plr_x = getFirst(player).x
  plr_y = getFirst(player).y
})

onInput("a", () => {
  getFirst(player).x -= 1
  plr_x = getFirst(player).x
  plr_y = getFirst(player).y
})


onInput("s", () => {
  getFirst(player).y += 1
  plr_x = getFirst(player).x
  plr_y = getFirst(player).y
})


onInput("d", () => {
  getFirst(player).x += 1
  plr_x = getFirst(player).x
  plr_y = getFirst(player).y
})

onInput("j", () => {
  addSprite(plr_x, plr_y, hoed_dirt);
  plr_x = getFirst(player).x
  plr_y = getFirst(player).y
})

afterInput(() => {
  
})
"""

errors_2 = '[{"description":"ReferenceError: a is not defined\n    at eval (index.bf7583b1.js:37:21)","raw":{},"line":37,"column":21}]'