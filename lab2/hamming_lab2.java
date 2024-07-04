import java.util.HashMap;
import java.util.Scanner;

public class hamming_lab2 {

    public static void main(String[] args) {
        HashMap<String, Integer> table = new HashMap<>(); // таблица для превода синдрома
        table.put("001", 3);
        table.put("010", 1);
        table.put("011", 5);
        table.put("100", 0);
        table.put("101", 4);
        table.put("110", 2);
        table.put("111", 6);
       
        // массив с позициями пр. разрядов
        int[] r_places = {1 - 1, 2 - 1, 4 - 1}; // -1, тк индексы идут с 0
        Scanner s = new Scanner(System.in);
        String request = s.nextLine(); // request - введенное число
        
        int sumer; // сюда поместим суммы проверочных разрядов для каждой степени двойки
        String syndrome = ""; // в эту строку будем помещать единицы и нули - синдром посл-ти
        
        for (int i: r_places) {
            sumer = 0;
            
            for (int j = i; j < request.length(); j++) {
                sumer = (((j + 1) / (i + 1)) % 2 == 1) ? sumer + Character.getNumericValue(request.charAt(j)) : sumer;
                // ^ выбираем проверочные разряды
            
            }
            syndrome = syndrome.concat(Integer.toString(sumer % 2)); // складываем рез-ты для каждой ст. двойки
        
        }
        
        String reversedSyndrome = new StringBuilder(syndrome).reverse().toString(); // развернём синдром
        
        if (!reversedSyndrome.equals("000")){
            int result = table.get(reversedSyndrome); // получаем номер ошибочного бита
            char[] pattern = request.toCharArray();
            pattern[result] = (pattern[result] == '1') ? '0' : '1';
            request = new String(pattern);
            System.out.printf("Номер ошибочного бита: %s, ответ: %s\n", result + 1, request);
        }
        else{
            System.out.println("Ошибочных битов нет");
        }
    }
}
