função soma_inferior (inteiro A[][], inteiro n):inteiro{
inteiro i, j, soma;
	soma <- 0;
para i -> 1 até n–1{
		para j -> 0 até i-1{
			soma <- soma + A[i][j]
		}
}
}
