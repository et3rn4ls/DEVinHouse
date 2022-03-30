import Produto from './Produto.js';
import { calculaTotal } from './utils.js';

const arroz = new Produto('arroz', 3, 9);
const feijao = new Produto('feijao', 2, 12);
const batata = new Produto('batata', 4, 8);
const macarrao = new Produto('macarrao', 1, 5);
const polenta = new Produto('[polenta]', 2, 5);

const total = calculaTotal(arroz, feijao, batata, macarrao, polenta);
console.log(`Valor total: R$ ${total}.00`);