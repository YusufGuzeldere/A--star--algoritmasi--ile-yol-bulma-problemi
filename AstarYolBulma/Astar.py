"""
Bu kod, bir labirentte (matris olarak temsil edilen) bir başlangıç noktasından bir son noktaya en kısa yolu bulmak için A* yol bulma algoritmasını kullanır. 
A* algoritması, bir arama algoritmasıdır ve başlangıç noktasından son noktaya en kısa yolu bulmak için kullanılır. Sınıf Node, izgaradaki her konumu temsil etmek için kullanılır. 
Bu sınıf, konum, g(n), h(n) ve f(n) değerlerini içermektedir. g(n) ,başlangıç noktasından geçerli noktaya olan gerçek mesafeyi temsil eder. h(n) ise heuristic fonksiyon ile 
geçerli noktadan bitiş noktasına olası olan en kısa yolu temsil eder. f(n) ise g(n) ve h(n) değerlerinin toplamıdır. A* algoritması, f(n) değerlerini kullanarak en kısa yolu bulur. 
Bu kod, open_list ve closed_list adlı iki liste kullanır. open_list, daha önce keşfedilmemiş düğümleri içerirken, closed_list daha önce keşfedilmiş düğümleri içermektedir. 
Bu kod, son noktaya ulaşana kadar open_list'te düğümleri sürekli olarak keşfeder ve closed_list'e ekler. Bulunan en kısa yol dizi olarak geri döndürülür.
"""
#Bu, ızgaradaki her konumu temsil etmek için kullanılan Düğüm sınıfı için bir sınıf tanımıdır
class Node():
    """A* Yol bulma için bir düğüm sınıfı"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    """pozisyon değiştirme"""
    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Verilen labirentte verilen başlangıçtan verilen sona giden bir yol olarak demetlerin bir listesini döndürür"""

    # Başlangıç ve bitiş düğümü oluştur
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Hem açık hem de kapalı listeyi başlat
    """
    Open_list, A* yol bulma algoritmasının bir parçası olarak, daha önce keşfedilmemiş düğümleri içermektedir.
    Bu düğümler, yol bulma algoritması tarafından daha önce incelenmemiş veya ziyaret edilmemiş olan düğümlerdir. 
    A* algoritması, open_list'te bulunan düğümleri sıralar ve her seferinde f(n) değerlerine göre en düşük olan düğümü seçerek, 
    geçerli düğüm olarak atar. Algoritma, geçerli düğümün çocuklarını (yani, geçerli düğümden ulaşılabilir olan diğer düğümleri) keşfeder 
    ve open_list'e ekler. Bu düğümler, geçerli düğümün çocukları olduğu için, h(n) ve g(n) değerleri için yeni değerler hesaplanır. 
    Bu şekilde, A* algoritması, geçerli düğümün çocukları arasından en kısa yolu bulmaya devam eder. Open_list, yol bulma algoritmasının daha önce
    keşfedilmemiş düğümleri takip etmesine ve bu düğümler arasından en kısa yolu bulmasına izin verir.
    """
    open_list = []  # uğranıp açılmayan düğümlerin listesi
    """
    Closed_list, A* yol bulma algoritmasının bir parçası olarak, daha önce ziyaret edilmiş veya incelenmiş olan düğümleri içermektedir. 
    Bu düğümler, yol bulma algoritması tarafından daha önce keşfedilmiş veya ziyaret edilmiş olan düğümlerdir. 
    Algoritma, open_list'te bulunan düğümleri sıralarken, daha önce ziyaret edilmiş olan düğümleri tekrar incelemez, yerine closed_list'te bulunan düğümleri atlar. 
    Bu sayede, algoritma daha önce ziyaret ettiği düğümleri tekrar ziyaret etmeden, yol bulma işlemi süresinde daha etkili olur. 
    Ayrıca, yol bulma algoritması, closed_list'te bulunan düğümler arasından bir düğüme geri dönmek için kullanılmaz. 
    Bu, yol bulma algoritmasının daha önce keşfedilmiş olan yolları tekrar incelemeden, daha hızlı ve daha verimli bir şekilde yol bulmasını sağlar.

    """


    closed_list = [] # uğrayıp açtığı düğümlerin listesi

    # Başlangıç düğümünü ekle
    open_list.append(start_node)

    # Sonunu bulana kadar döngü
    while len(open_list) > 0:

        # Geçerli düğümü al
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Geçerli açık listeden çıkar, kapalı listeye ekle
        # en yakın f(n) değerine göre seçilen düğümü openlistten çıkarır closedlist e 
       
        open_list.pop(current_index)
        closed_list.append(current_node)

        # hedefi buldum
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Tersine dönüş yolu

        # Çocuk oluştur
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # bitişik kareler

            # geçerli düğümün komşu düğümlerinin koordinatlarını hesaplamak için kullanılır.
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # geçerli düğümün komşu düğümlerinin labirent içinde olup olmadığını kontrol eder.
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #geçerli düğümün komşu düğümlerinin geçilebilir olup olmadığını kontrol eder
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # mevcut düğümün parent olarak ve node_position'ı pozisyon olarak kullanarak yeni bir düğüm nesnesi oluşturur
            new_node = Node(current_node, node_position)

            # Ekle
            children.append(new_node)

        # Çocuklar arasında döngü
        for child in children:

            # Bu döngü içinde, her çocuk düğüm için closed_list adlı dizideki tüm düğümler kontrol edilir. 
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Bu kod satırı, çocuk düğümün maliyetini hesaplamak için kullanılır.
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Bu kod satırı, çocuk düğümün open_list adlı dizide zaten mevcut olup olmadığını ve eğer mevcutsa, 
            # çocuk düğümün g değerinin open_list dizisindeki aynı düğümün g değerinden daha yüksek olup olmadığını kontrol etmek için kullanılır.
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Bu çocuk düğüm, daha önce keşfedilmemiş veya daha iyi bir yol bulunmamış olduğu için open_list adlı listesine eklenir.
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (9, 9)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()