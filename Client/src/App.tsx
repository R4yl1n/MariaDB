import React from 'react'
import { Box, List, ThemeIcon } from '@mantine/core'
import './App.css'
import useSWR from 'swr';

export interface datas {
  vorname:string;
  nachname: string;
  telnummer: string;
}

const fetcher = (...args) => fetch(...args).then((res) => res.json());

function App() {

  const {data,error} = useSWR('http://localhost:4000/api/datas/', fetcher)
  const test = "testing if this works"

  return (
    <div>
        {data}
    </div>
  )
  }
export default App
  