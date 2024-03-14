class IMC:
    @staticmethod
    def calc(weight, height):
        if weight == 0:
            return 0
        
        height_meters = height / 100
        return weight / (height_meters * height_meters)
    
if __name__ == '__main__':
    weight = float(input('Informe seu peso em kilos: '))
    height = int(input('Informe sua altura em centímetros: '))
    imc = IMC.calc(weight, height)
    print(f'Seu IMC é {imc:.2f}')