package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"

	"adventofcode/2015/util"
)

var lights = [1000][1000]int{}

func main() {
	var f io.Reader
	var err error
	f, err = os.Open("2015/day6/input.txt")
	util.CheckError(err)

	s := bufio.NewScanner(f)
	for s.Scan() {
		parse(s.Text())
	}
	fmt.Println(lights)
	fmt.Printf("Sum: %d\n", sum(lights))
}

func sum(arr [1000][1000]int) int {
	res := 0
	for _, x := range arr {
		for _, y := range x {
			res += y
		}
	}
	return res
}

func parse(line string) {
	startX, startY, endX, endY := getCorners(line)
	if strings.HasPrefix(line, "turn on") {
		flood(startX, startY, endX, endY, 1)
	} else if strings.HasPrefix(line, "turn off") {
		flood(startX, startY, endX, endY, 1)
	} else if strings.HasPrefix(line, "toggle") {
		toggle(startX, startY, endX, endY)
	}
}

func getInt(x string) int {
	y, _ := strconv.Atoi(x)
	return y
}

func getCorners(line string) (int, int, int, int) {
	re, _ := regexp.Compile("\\d+")
	c := re.FindAllString(line, -1)
	return getInt(c[0]), getInt(c[1]), getInt(c[2]), getInt(c[3])
}

func flood(startX int, startY int, endX int, endY int, val int) {
	for x := startX; x <= endX; x++ {
		for y := startY; y <= endY; y++ {
			lights[y][x] = val
		}
	}

}

func toggle(startX int, startY int, endX int, endY int) {
	for x := startX; x <= endX; x++ {
		for y := startY; y <= endY; y++ {
			cur := lights[y][x]
			if cur == 0 {
				lights[y][x] = 1
			} else {
				lights[y][x] = 0
			}
		}
	}
}
