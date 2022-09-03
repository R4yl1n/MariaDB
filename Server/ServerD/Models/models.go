package models

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
	_ "github.com/microsoft/go-mssqldb"
)

type MariaDB struct {
	Vorname   string `json:"vorname"`
	Nachname  string `json:"nachname"`
	Telnummer string `json:"telnummer"`
}

var server = "myphonebook.database.windows.net"
var port = 1433
var user = "DeBoss"
var password = "Neonalbaner8953"
var database = "DeBoss"

func Getall() []MariaDB {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err := sql.Open("sqlserver", connString)
	if err != nil {
		log.Panic(err)
	}
	log.Println("Get Request Done")
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

func Inserdata(body MariaDB) []MariaDB {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err := sql.Open("sqlserver", connString)
	if err != nil {
		log.Panic(err)
	}
	log.Printf("Post request Done of %v", body)
	defer db.Close()

	ready := fmt.Sprintf(`INSERT INTO infos(Vorname, Nachname, Telnummer) VALUES('%s','%s','%s')`, body.Vorname, body.Nachname, body.Telnummer)
	_, err = db.Exec(ready)
	if err != nil {
		log.Fatal("while Inserting an error ocurred \n", err)
	}
	resp := Getall()
	return resp
}

func Replacenumber(body MariaDB) []MariaDB {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err := sql.Open("sqlserver", connString)
	if err != nil {
		log.Panic(err)
	}
	log.Printf("Patch request Done for %v", body)
	defer db.Close()

	_, err = db.Exec(`UPDATE infos SET Telnummer=? Where Vorname=? && Nachname=?`, body.Telnummer, body.Vorname, body.Nachname)
	if err != nil {
		log.Fatal("while replacing the number an error ocurred \n", err)
	}
	resp := Getall()
	return resp
}

func Deletedatas(body MariaDB) string {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err := sql.Open("sqlserver", connString)
	if err != nil {
		log.Panic(err)
	}
	log.Printf("Delete request Done for %v", body)
	defer db.Close()

	ready := fmt.Sprintf(`DELETE FROM infos WHERE Vorname='%s' AND Nachname='%s'`, body.Vorname, body.Nachname)
	_, err = db.Exec(ready)
	if err != nil {
		log.Fatal(err)
	}
	Getall()
	return "Succesfully deleted " + " " + body.Vorname + " " + body.Nachname + " " + body.Telnummer
}

func Getjust(vorname string) []MariaDB {
	connString := fmt.Sprintf("server=%s;user id=%s;password=%s;port=%d;database=%s;",
		server, user, password, port, database)

	db, err := sql.Open("sqlserver", connString)
	if err != nil {
		log.Panic(err)
	}
	log.Println("Get Request Done")
	defer db.Close()

	ready := fmt.Sprintf(`SELECT * FROM infos WHERE Vorname='%s'`, vorname)
	rows, _ := db.Query(ready)
	if err != nil {
		log.Fatal("error 1// ", err)
	}

	mariadatas := make([]MariaDB, 0)
	for rows.Next() {
		var mariadb MariaDB
		err2 := rows.Scan(&mariadb.Vorname, &mariadb.Nachname, &mariadb.Telnummer)
		if err2 != nil {
			log.Fatal("error 2// ", err2)
		}
		mariadatas = append(mariadatas, mariadb)
	}
	log.Println(mariadatas)
	return mariadatas

}
