void pilha_fundir(pilha*p1, pilha*p2){
    pilha aux1, aux2, resultado;
    aux1.topo = -1;
    aux2.topo = -1;
    resultado.topo = -1;

    while (!stack_isempty(*p1))
        push(&aux1, pop(p1));

    while (!stack_isempty(*p2))
        push(&aux2, pop(p2));

    while (!stack_isempty(aux1)) {
        int valor = pop(&aux1);
        push(p1, valor);
        push(&resultado, valor);
    }

    while (!stack_isempty(aux2)) {
        int valor = pop(&aux2);
        push(p2, valor);
        push(&resultado, valor);
    }

    return resultado;
}