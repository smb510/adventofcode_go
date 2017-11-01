package main

import (
"io/ioutil"
"github.com/example/project/2015/util"
)

func main() {
	_, err := ioutil.ReadFile("2015/day1/input.txt")
	util.CheckError(err)
}
