package main

import (
	"log"

	"github.com/R4yl1n/MariaDB/models"
	"github.com/gofiber/fiber/v2"
)

var responseDB = make([]models.MariaDB, 0)

func main() {

	app := fiber.New()

	app.Get("api/getall", func(c *fiber.Ctx) error {
		responseDB = models.Getall()
		log.Print(responseDB)

		return c.JSON(responseDB)
	})

	log.Fatal(app.Listen(":4000"))
}
