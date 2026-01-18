from datetime import datetime, timedelta

def calcular_data_migracao():
    data_input = input("Informe a data da solicitação da denúncia (DD/MM/AAAA): ")

    try:
        # Converte a data informada
        data_denuncia = datetime.strptime(data_input, "%d/%m/%Y")

        # Soma 180 dias
        data_180 = data_denuncia + timedelta(days=180)

        # Se já for dia 01, mantém
        if data_180.day == 1:
            data_migracao = data_180
        else:
            # Vai para o primeiro dia do próximo mês
            if data_180.month == 12:
                data_migracao = datetime(data_180.year + 1, 1, 1)
            else:
                data_migracao = datetime(data_180.year, data_180.month + 1, 1)

        print("\n📅 Resultado:")
        print(f"Data da solicitação da denúncia: {data_denuncia.strftime('%d/%m/%Y')}")
        print(f"Data da migração: {data_migracao.strftime('%d/%m/%Y')}")

    except ValueError:
        print("❌ Data inválida. Use o formato DD/MM/AAAA.")


calcular_data_migracao()