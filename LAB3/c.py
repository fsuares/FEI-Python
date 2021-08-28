vazao = float(input("Digite a vazão da bomba em l/s: "))
capacidade = float(input("Digite a capacidade do reservatório: "))
seg_total = capacidade/vazao
min_total = seg_total // 60
hor = min_total // 60
min = min_total % 60
seg = seg_total % 60

print("Tempo necessário para encher o reservatório: {:.0f}:{:.0f}:{:.0f}".format(hor,min,seg))