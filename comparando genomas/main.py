entrada = open("comparando genomas/18s_humano.fasta").read()
saida = open("comparando genomas/humano.html","w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "")
entrada = entrada.replace("N", "G")

for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

i = 0
for k in cont:
    transparencia = cont[k]/max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0, 0, 0,"+str(transparencia)+"')></div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")

    i+=1

saida.close()