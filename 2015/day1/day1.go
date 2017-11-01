package main

import (
"io/ioutil"
"github.com/example/project/2015/util"
)

func main() {
	_, err := ioutil.ReadFile("input.txt")
	util.CheckError(err)
}
