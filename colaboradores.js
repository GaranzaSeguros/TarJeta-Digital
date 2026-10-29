/* ============================================================
   COLABORADORES. Una entrada por persona.
   La tarjeta de cada quien se abre con:  index.html?c=<clave>
   Sin "?c=" se muestra la de la primera entrada (gortega).

   pila / apellidos : como se guardan en la agenda del telefono
   puesto, email    : lo que aparece en la tarjeta
   celular          : llamar, WhatsApp y guardar contacto ("" si no tiene)
   ext              : extension de la oficina ("" si no tiene)
   oficina          : true si se muestra el telefono de oficina
   corto            : (opcional) como se le saluda en WhatsApp; por defecto, su primer nombre
   linkedin         : (opcional) su perfil propio; si no, se usa el de la empresa
   foto             : (opcional) por defecto fotos/<clave>.jpg ; si no existe, no se muestra
   ============================================================ */
const COLABORADORES = {
  gortega:      { pila: "Guillermo",             apellidos: "Ortega Reyes",        puesto: "Director General",                        email: "gortega@garanza.com.mx",       celular: "55 1474 5018", ext: "3207", oficina: true },
  isanchez:     { pila: "L. Ivonne",             apellidos: "Sánchez Vega",        puesto: "Directora de Operaciones",                email: "isanchez@garanza.com.mx",      celular: "55 1474 1798", ext: "3205", oficina: true, corto: "Ivonne" },
  ccampos:      { pila: "Carolina",              apellidos: "Campos Hernández",    puesto: "Gerente Administrativo",                  email: "ccampos@garanza.com.mx",       celular: "55 8017 0581", ext: "3212", oficina: true },
  faguilar:     { pila: "Fernando",              apellidos: "Aguilar Ibáñez",      puesto: "Mensajero",                               email: "faguilar@garanza.com.mx",      celular: "55 3880 9730", ext: "3220", oficina: true },
  esanchez:     { pila: "Saul Enrique",          apellidos: "Sánchez Vega",        puesto: "Jefe de Producción y Cancelaciones",      email: "esanchez@garanza.com.mx",      celular: "55 8017 0580", ext: "3203", oficina: true },
  adelamora:    { pila: "Alexa",                 apellidos: "De la Mora García",   puesto: "Becaria",                                 email: "adelamora@garanza.com.mx",     celular: "",             ext: "3208", oficina: true },
  rgallegos:    { pila: "Rosa",                  apellidos: "Gallegos Heredia",    puesto: "Jefa de Promotoría",                      email: "rgallegos@garanza.com.mx",     celular: "55 8017 0587", ext: "3216", oficina: true },
  vrodriguez:   { pila: "Valeria",               apellidos: "Rodríguez Martínez",  puesto: "Auxiliar Administrativo",                 email: "vrodriguez@garanza.com.mx",    celular: "55 6465 0289", ext: "3210", oficina: true },
  mgarcia:      { pila: "María",                 apellidos: "García Hernández",    puesto: "Coordinadora de Operaciones",             email: "mgarcia@garanza.com.mx",       celular: "55 8017 0583", ext: "3214", oficina: true },
  jlopez:       { pila: "Juana",                 apellidos: "López Frausto",       puesto: "Jefa de Operaciones",                     email: "jlopez@garanza.com.mx",        celular: "55 8017 0582", ext: "3219", oficina: true },
  stvillanueva: { pila: "Servio Tulio",          apellidos: "Villanueva Palma",    puesto: "Subdirector Jurídico",                    email: "stvillanueva@garanza.com.mx",  celular: "55 4331 7275", ext: "",     oficina: false },
  cvillanueva:  { pila: "Cristian",              apellidos: "Villanueva Palma",    puesto: "Abogado",                                 email: "cvillanueva@garanza.com.mx",   celular: "55 5401 1578", ext: "",     oficina: false },
  rislas:       { pila: "Rocío",                 apellidos: "Islas Aragón",        puesto: "Ejecutiva de Siemens",                    email: "rocio.islas_aragon.ext@siemens-energy.com", celular: "55 8022 3455", ext: "", oficina: false },
  atorres:      { pila: "Ana Laura",             apellidos: "Torres",              puesto: "Ejecutiva de Cuenta",                     email: "atorres@garanza.com.mx",       celular: "55 8017 0584", ext: "",     oficina: false },
  mmendez:      { pila: "Mauricio Agdabel",      apellidos: "Méndez Ávila",        puesto: "Auxiliar Administrativo",                 email: "mmendez@garanza.com.mx",      celular: "55 4090 9512", ext: "",     oficina: true },
  avilla:       { pila: "Alejandro",             apellidos: "Villa",               puesto: "Auxiliar Administrativo",                 email: "avilla@garanza.com.mx",                           celular: "55 8006 1052", ext: "3202", oficina: true }
};
