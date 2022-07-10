package models

import (
	"database/sql"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

type MariaDB struct {
	Vorname   string `json:"vorname"`
	Nachname  string `json:"nachname"`
	Telnummer string `json:"telnummer"`
}

func Getall() []MariaDB {
	db, err := sql.Open("mysql", "root:Admin1234!@tcp(192.168.1.246:3306)/test?parseTime=True")
	if err != nil {
		log.Panic(err)
	}
	log.Println("connected succesfuly to the DB")
	defer db.Close()

	rows, _ := db.Query(`SELECT * FROM infos`)
	if err != nil {
		log.Fatal("error 1// ", err)
	}

	i := 0
	mariadatas := make([]MariaDB, 0)

	for rows.Next() {
		var mariadb MariaDB
		err2 := rows.Scan(&mariadb.Vorname, &mariadb.Nachname, &mariadb.Telnummer)
		if err2 != nil {
			log.Fatal("error 2// ", err2)
		}
		mariadatas = append(mariadatas, mariadb)

		i++
	}
	log.Println(mariadatas)
	return mariadatas
}

func Inserdata(vorname string, nachname string, telnummer string) {
	db, err := sql.Open("mysql", "root:Admin1234!@tcp(192.168.1.246:3306)/test?parseTime=True")
	if err != nil {
		log.Panic(err)
	}
	defer db.Close()

	_, err = db.Exec(`INSERT INTO infos(Vorname, Nachname, Telnummer) VALUES(?,?,?)`,
		vorname, nachname, telnummer)
	if err != nil {
		log.Fatal("while Inserting an error ocurred \n", err)
	}
	Getall()
}

func Replacenumber(vorname string, nachname string, to string) {
	db, err := sql.Open("mysql", "root:Admin1234!@tcp(192.168.1.246:3306)/test?parseTime=True")
	if err != nil {
		log.Panic(err)
	}
	defer db.Close()

	_, err = db.Exec(`UPDATE infos SET Telnummer=? Where Vorname=? && Nachname=?`, to, vorname, nachname)
	if err != nil {
		log.Fatal("while replacing the number an error ocurred \n", err)
	}
	Getall()
}

func Deletedatas(vorname string, nachname string) {
	db, err := sql.Open("mysql", "root:Admin1234!@tcp(192.168.1.246:3306)/test?parseTime=True")
	if err != nil {
		log.Panic(err)
	}
	defer db.Close()

	_, err = db.Exec(`DELETE FROM infos WHERE Vorname=? && Nachname=?`, vorname, nachname)
	if err != nil {
		log.Fatal(err)
	}
	Getall()
}
