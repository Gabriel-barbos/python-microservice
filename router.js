import Carrinho from "./carrinho";
import Login from "./login";
import Pedidos from "./pedido";
import  Produto from './produto';

let rotas;
export default rotas = {
    "#login": {
        component: Login,
        meta: {
            title: "SPA - Login",
            description: "Página A",
        },
    },
    "#pedido": {
        component: Pedidos,
        meta: {
            title: "SPA - pedidos",
            description: "Página B",
        },
    },
    "#pedido": {
        component: Carrinho,
        meta: {
            title: "SPA - carrinho",
            description: "Página c",
        },
    },
    "#produto": {
        component: Produto,
        meta: {
            title: "SPA - produto",
            description: "Página D",
        },
    },
};


