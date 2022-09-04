package main

import (
	"fmt"
	"time"

	"github.com/abdfnx/gosh"
)

func main() {
	osIsValid()
}

func osIsValid() {
	fmt.Println("which Terminal are you using currently? powershell or bash")
	var answer string
	fmt.Scan(&answer)

	switch answer {
	case "powershell":
		fmt.Println("you picked poweshell")
		gosh.PowershellCommand(`
		cd Server

		docker build ./

		cd ..

		cd Flask

		docker build ./
		`)

	case "bash":
		fmt.Println("you picked bash")
		gosh.ShellCommand(`
		cd Server

		docker build ./

		cd ..

		cd Flask

		docker build ./
		`)

	default:
		fmt.Println("please check how you wrote it. you have to write it the right way")
		time.Sleep(1500 * time.Millisecond)
		osIsValid()
	}
}
