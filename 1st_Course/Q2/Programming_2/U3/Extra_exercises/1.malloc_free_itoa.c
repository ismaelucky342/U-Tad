#include<stdio.h>
#include<stdlib.h>

char	*ft_itoa(int n);
static int	ft_digit_counter(int n);

int main()
{
    int n = -2147483648;
    char *str = ft_itoa (n);

    if (str == NULL)
    printf("Error al convertir el número %d a cadena.\n",(n));

    printf("%s\n", str);
    free(str);

    return (0);
}

static int	ft_digit_counter(int n)
{
	int		count;

	count = 0;
	if (n == 0)
		return (1);
	if (n < 0)
		count++;
	while (n != 0)
	{
		n /= 10;
		count++;
	}
	return (count);
}

char	*ft_itoa(int n)
{
	int		ncpy;
	int		i;
	char	*str;

	if (n == -2147483648)
		return (ft_strdup("-2147483648"));
	ncpy = n;
	if (n < 0)
		ncpy = -n;
	i = ft_digit_counter(n);
	str = malloc(sizeof(char) * (i + 1));
	if (!str)
		return (NULL);
	str[i] = '\0';
	i--;
	if (ncpy == 0)
		str[i] = '0';
	while (ncpy > 0)
	{
		str[i--] = (ncpy % 10) + '0';
		ncpy /= 10;
	}
	if (n < 0)
		str[0] = '-';
	return (str);
}
