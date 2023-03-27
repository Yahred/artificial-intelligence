class Solution(object):
    def isPalindrome(self, x):
        
        """
        :type x: int
        :rtype: bool
        """

        cadena = str(x)

        for i in range(len(cadena.split())):
            volteada = cadena.split()[len(cadena) - i - 1]
        return True if volteada == cadena else False

# Creamos una instancia de la clase Solution
solucion = Solution()

# Llamamos al método isPalindrome con un número entero
resultado = solucion.isPalindrome(121)

# Imprimimos el resultado
print(resultado)
