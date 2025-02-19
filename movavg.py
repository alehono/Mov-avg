import numpy as np

def movavg(data, window):
     average_data = []
     for ind in range(len(data) - window + 1):
          average_data.append(np.mean(data[ind:ind+window]))
     return average_data

def movavg2(data, window):
    i_data = []
    average_data = []
    i = 0
    while i < len(data) - window + 1:
     average_data.append(np.mean(data[i:i+window]))
     i_data.append(i+1)
     i = i + window
    print("fim do cálculo!")
    return i_data, average_data

def dynamic_moving_average(data, window_size):
    """
    Calcula a média móvel com janela dinâmica, centrada no ponto atual,
    garantindo que o número de elementos usados seja consistente com o tamanho da janela.
    
    Args:
        data (list ou array): Série de dados para calcular a média móvel.
        window_size (int): Tamanho máximo da janela para a média móvel.
    
    Returns:
        list: Série suavizada com a média móvel.
    """
    half_window = window_size // 2
    smoothed_data = []
    i_data = []

    for i in range(len(data)):
        # Ajusta os limites da janela dinamicamente
        start = max(0, i - half_window)
        end = min(len(data), i + half_window)

        # Garante que a janela sempre terá o tamanho especificado
        # Expandindo para frente ou para trás, se necessário
        while end - start < window_size:
            if start > 0:
                start -= 1  # Expande para trás
            elif end < len(data):
                end += 1  # Expande para frente
            else:
                break  # Não há mais como expandir

        # Extrai os dados da janela e calcula a média
        window = data[start:end]
        smoothed_data.append(sum(window) / len(window))
        i_data.append(i+1)

    return i_data, smoothed_data