void pilha_remover_ocorrencias(pilha* p, stack_info valor){

    pilha aux;
    stack_init(&aux);

    stack_info temp;

    while(!stack_isempty(*p)){
        temp = pop(p);

        if(temp != valor){
            push(&aux, temp);
        }
    }

    while (!stack_isempty(aux)){
        push(p, pop(&aux));
    }