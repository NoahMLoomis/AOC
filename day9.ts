const file = Deno.readTextFileSync("./data/day9.txt",);
const data = file.split("\n")

const direction = data[0].split(" ")[0]
const movement = Number(data[0].split(" ")[1])

const rope = {
    head: {
        x: 0,
        y: 0
    },
    tail: {
        x: 0,
        y: 0
    }
}

const moveTail = () => {
    if (rope.head.x > rope.tail.x) {
        rope.tail.x += 1
    } else if (rope.head.x < rope.tail.x) {
        rope.tail.x -= 1
    } else if (rope.head.y > rope.tail.y) {
        rope.tail.y += 1
    } else if (rope.head.y < rope.tail.y) {
        rope.tail.y -= 1
    }
}

data.forEach((item) => {
    const direction = item.split(" ")[0]
    const movement = Number(item.split(" ")[1])

    for (let i = 0; i < movement; i++) {
        if (direction === "U") {
            rope.head.y += 1
        } else if (direction === "D") {
            rope.head.y -= 1
        } else if (direction === "R") {
            rope.head.x += 1
        } else if (direction === "L") {
            rope.head.x -= 1
        }
        moveTail()
    }
})