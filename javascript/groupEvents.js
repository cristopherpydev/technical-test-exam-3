/*
Dado el siguiente array:

const events = [
  { type: "click", user: "A" },
  { type: "scroll", user: "B" },
  { type: "click", user: "A" },
  { type: "click", user: "C" }
];
Implementa una función que devuelva un objeto con el número de eventos por tipo:

Resultado esperado:

{
  click: 3,
  scroll: 1
}*/


function contar_interacciones(){
  const events = [
  { type: "click", user: "A" },
  { type: "scroll", user: "B" },
  { type: "click", user: "A" },
  { type: "click", user: "C" }
  ];

  const contabilizacion_clicks = events.reduce((acc, cur) => cur.type === "click" ? ++acc : acc, 0);
  const contabilizacion_scroll = events.reduce((acc, cur) => cur.type === "scroll" ? ++acc : acc, 0);
  
  array_objeto = {clicks: contabilizacion_clicks, scroll: contabilizacion_scroll}

}
