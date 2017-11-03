import(
"os"
"io"
"bufio"
"fmt"

"adventofcode/2015/util"
)

func main() {
var f io.Reader
	var err error
	f, err = os.Open("2015/day1/input.txt")
	defer f.Close()
	util.CheckError(err)

	s := bufio.NewScanner(f)
	for s.Scan() {
		fmt.Println(s.Text())
	}
}