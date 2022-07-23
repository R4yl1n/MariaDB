import React from 'react'
import { Box, List, ThemeIcon } from '@mantine/core'
import './App.css'
import useSWR from 'swr';

export interface datas {
  vorname:string;
  nachname: string;
  telnummer: string;
}

class person {
  constructor(vorname, nachname, telnummer) {
    this.vorname = vorname;
    this.nachname = nachname;
    this.telnummer = telnummer;
  }
}

const fetcher = (...args) => fetch(...args).then((res) => res.json());

function App() {

  const {data,error} = useSWR('http://localhost:4000/api/datas/', fetcher)
   

  
  for (var key in data){
    if (data.hasOwnProperty(key)) {
      var vorname = (data[key].vorname);
      var nachname = (data[key].nachname);
      var telnummer = (data[key].telnummer);

      var   =new person(vorname,nachname,telnummer)
    }
    }


  return (
    <div>
      <p>{vorname}</p>
      <p>{nachname}</p>
      <p>{telnummer}</p>
    </div>
  )
  }
export default App
  