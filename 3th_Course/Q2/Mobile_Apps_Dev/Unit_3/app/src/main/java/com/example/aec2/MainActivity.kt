package com.example.aec2

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.aec2.ui.theme.AEC2Theme

// Color corporativo U-tad (Azul vivo)
val UtadBlue = Color(0xFF0054A6)
val DisplayBackground = Color(0xFFD1E8E2) // Color verdoso tipo pantalla Casio antigua

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AEC2Theme {
                Scaffold(
                    modifier = Modifier.fillMaxSize(),
                    containerColor = Color(0xFFF0F0F0) // Fondo gris claro
                ) { innerPadding ->
                    CalculatorScreen(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}

@Composable
fun CalculatorScreen(modifier: Modifier = Modifier) {
    var expression by remember { mutableStateOf("") }
    var currentInput by remember { mutableStateOf("0") }
    var result by remember { mutableStateOf<Int?>(null) }
    var isNewOperation by remember { mutableStateOf(true) }

    Column(
        modifier = modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        // Logo U-tad
        Text(
            text = "u-tad",
            color = UtadBlue,
            fontSize = 32.sp,
            fontWeight = FontWeight.ExtraBold,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        // Casio Style Display
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .weight(0.3f)
                .background(DisplayBackground, RoundedCornerShape(8.dp))
                .padding(16.dp),
            verticalArrangement = Arrangement.SpaceBetween
        ) {
            // Línea de la operación (Expression)
            Text(
                text = expression,
                style = MaterialTheme.typography.bodyLarge,
                color = Color.DarkGray,
                modifier = Modifier.fillMaxWidth(),
                textAlign = TextAlign.End,
                maxLines = 1
            )
            // Línea del número actual o resultado
            Text(
                text = if (result != null) result.toString() else currentInput,
                style = MaterialTheme.typography.displayMedium,
                fontWeight = FontWeight.Bold,
                color = Color.Black,
                modifier = Modifier.fillMaxWidth(),
                textAlign = TextAlign.End,
                maxLines = 1
            )
        }

        Spacer(modifier = Modifier.height(16.dp))

        // Buttons Grid
        val buttons = listOf(
            listOf("7", "8", "9", "C", "/"),
            listOf("4", "5", "6", "DEL", "*"),
            listOf("1", "2", "3", "(", "-"),
            listOf("0", "±", ".", ")", "+"),
            listOf("=")
        )

        Column(
            modifier = Modifier.weight(0.7f),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            buttons.forEach { row ->
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    row.forEach { symbol ->
                        CalculatorButton(
                            symbol = symbol,
                            modifier = if (symbol == "=") Modifier.fillMaxWidth() else Modifier.weight(1f),
                            onClick = {
                                when {
                                    symbol.all { it.isDigit() } -> {
                                        if (isNewOperation) {
                                            currentInput = symbol
                                            isNewOperation = false
                                        } else {
                                            currentInput = if (currentInput == "0") symbol else currentInput + symbol
                                        }
                                        result = null
                                    }
                                    symbol == "C" -> {
                                        expression = ""
                                        currentInput = "0"
                                        result = null
                                        isNewOperation = true
                                    }
                                    symbol == "DEL" -> {
                                        if (currentInput.length > 1) {
                                            currentInput = currentInput.dropLast(1)
                                        } else {
                                            currentInput = "0"
                                            isNewOperation = true
                                        }
                                    }
                                    symbol == "=" -> {
                                        if (expression.isNotEmpty() || !isNewOperation) {
                                            val fullExpr = if (isNewOperation) expression else expression + currentInput
                                            result = evaluateExpression(fullExpr)
                                            expression = "$fullExpr ="
                                            currentInput = "0"
                                            isNewOperation = true
                                        }
                                    }
                                    symbol in listOf("+", "-", "*", "/") -> {
                                        expression += currentInput + " " + symbol + " "
                                        currentInput = "0"
                                        isNewOperation = true
                                        result = null
                                    }
                                }
                            }
                        )
                    }
                }
            }
        }
    }
}

// Función simple para evaluar la cadena de texto (solo enteros como pide el ejercicio)
fun evaluateExpression(expr: String): Int {
    return try {
        // Esta es una implementación simplificada. Para algo real "complejo" se usaría un parser.
        // Aquí simulamos el cálculo secuencial (no prioridad de operadores para mantenerlo simple pero funcional)
        val tokens = expr.trim().split(" ")
        if (tokens.isEmpty()) return 0
        
        var res = tokens[0].toIntOrNull() ?: 0
        var i = 1
        while (i < tokens.size - 1) {
            val op = tokens[i]
            val nextVal = tokens[i+1].toIntOrNull() ?: 0
            res = when (op) {
                "+" -> res + nextVal
                "-" -> res - nextVal
                "*" -> res * nextVal
                "/" -> if (nextVal != 0) res / nextVal else 0
                else -> res
            }
            i += 2
        }
        res
    } catch (_: Exception) {
        0
    }
}

@Composable
fun CalculatorButton(
    symbol: String,
    modifier: Modifier = Modifier,
    onClick: () -> Unit
) {
    val isOperator = symbol in listOf("+", "-", "*", "/", "=", "C", "DEL", "(", ")", "±")
    val isAction = symbol == "="
    
    Button(
        onClick = onClick,
        modifier = modifier.height(60.dp),
        shape = RoundedCornerShape(4.dp), // Botones más rectangulares tipo Casio
        colors = ButtonDefaults.buttonColors(
            containerColor = when {
                isAction -> UtadBlue
                isOperator -> Color(0xFF444444) // Gris oscuro para operadores
                else -> Color.White // Blanco para números
            },
            contentColor = if (isOperator || isAction) Color.White else Color.Black
        ),
        elevation = ButtonDefaults.buttonElevation(defaultElevation = 4.dp),
        contentPadding = PaddingValues(0.dp)
    ) {
        Text(
            text = symbol,
            fontSize = if (symbol.length > 1) 16.sp else 20.sp,
            fontWeight = FontWeight.Bold
        )
    }
}

@Preview(showBackground = true)
@Composable
fun CalculatorPreview() {
    AEC2Theme {
        CalculatorScreen()
    }
}
