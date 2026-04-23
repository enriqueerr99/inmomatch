# 📋 Typeform Calculadora Setup
## Instrucciones para crear la calculadora interactiva

---

## 🔧 SETUP RÁPIDO

### Paso 1: Crear Typeform en typeform.com
1. Ve a https://typeform.com
2. Haz login o crea cuenta
3. Click "Create a new form"
4. Selecciona "Blank form"
5. Título: "Descubre cuándo puedes dejar tu trabajo"

---

## ✅ ESTRUCTURA DE PREGUNTAS (13 total)

### BLOQUE 1: DÓNDE ESTÁS AHORA (5 preguntas)

**Q1: Hola, ¿cuál es tu nombre?**
```
Tipo: Short text
Placeholder: "Tu nombre"
Obligatorio: Sí
Campo de variable: name
```

**Q2: ¿En qué ciudad o región vives?**
```
Tipo: Short text
Placeholder: "Ej: Madrid, Barcelona, Valencia..."
Obligatorio: Sí
Campo de variable: city
```

**Q3: ¿Cuál es tu trabajo actual?**
```
Tipo: Short text
Placeholder: "Ej: Programador, Vendedor, Abogado..."
Obligatorio: Sí
Campo de variable: job
```

**Q4: ¿Cuánto ganas al mes (neto)?**
```
Tipo: Number
Placeholder: "En €"
Min: 500
Max: 10000
Obligatorio: Sí
Campo de variable: monthly_income
```

**Q5: ¿Cuántos ahorros tienes ahora?**
```
Tipo: Number
Placeholder: "En €"
Min: 0
Max: 100000
Obligatorio: Sí
Campo de variable: savings
```

---

### BLOQUE 2: TIEMPO Y REALIDAD (3 preguntas)

**Q6: ¿Cuántas horas a la semana tienes LIBRES reales?**
```
Tipo: Number
Placeholder: "0-40 horas"
Min: 0
Max: 40
Obligatorio: Sí
Campo de variable: free_hours
Descripción: "Serio, no te juzgo si son 2 horas"
```

**Q7: ¿En qué momento tienes ese tiempo libre?**
```
Tipo: Multiple choice (checkbox)
Opciones:
  □ Mañanas (6-9am)
  □ Mediodías (12-14h)
  □ Tardes (18-21h)
  □ Noches (21-24h)
  □ Fines de semana

Obligatorio: Sí (mínimo 1)
Campo de variable: time_slots
```

**Q8: ¿Has probado algún otro negocio antes?**
```
Tipo: Multiple choice (radio)
Opciones:
  ○ No, sería mi primer intento
  ○ Sí, pero no funcionó
  ○ Sí, y me fue bastante bien
  ○ Sí, pero nunca llegué a cerrar

Obligatorio: Sí
Campo de variable: previous_business
```

---

### BLOQUE 3: LO QUE QUIERES (3 preguntas)

**Q9: ¿Cuándo te gustaría dejar tu trabajo?**
```
Tipo: Multiple choice (radio)
Opciones:
  ○ Ya, estoy quemado
  ○ En 3 meses
  ○ En 6 meses
  ○ En 1 año
  ○ Sin prisa, cuando sea

Obligatorio: Sí
Campo de variable: timeline
```

**Q10: ¿Te gustaría trabajar desde donde quisieras, sin horarios fijos?**
```
Tipo: Multiple choice (radio)
Opciones:
  ○ Sí, eso sería increíble
  ○ Sí, pero necesitaría algo de estructura
  ○ No, prefiero horario fijo
  ○ Me da igual

Obligatorio: Sí
Campo de variable: location_freedom
```

**Q11: ¿Cuál es tu sueño REAL si pudieras tener libertad?**
```
Tipo: Long text
Placeholder: "Ej: Viajar 3 meses al año, trabajar desde una playa..."
Obligatorio: No
Campo de variable: real_dream
```

---

### BLOQUE 4: LA OFERTA (2 preguntas)

**Q12: ¿Te parece razonable ganar €5,000-€15,000 por venta?**
```
Tipo: Multiple choice (radio)
Opciones:
  ○ Sí, suena increíble
  ○ Sí, pero suena difícil
  ○ Quizá, no sé si sea realista
  ○ No, me parece mucho

Obligatorio: Sí
Campo de variable: earning_potential
```

**Q13: Si todo esto fuera posible, ¿te interesaría aprender cómo hacerlo?**
```
Tipo: Multiple choice (radio)
Opciones:
  ○ Sí, totalmente
  ○ Quizá, depende del precio/contenido
  ○ No sé, necesito más info
  ○ No, no me interesa

Obligatorio: Sí
Campo de variable: interest_level
```

---

## 🎨 DISEÑO Y FORMATO

### Colores (según design-system.md)
- **Primary:** #0EA5E9 (Sky Blue)
- **CTA:** #F97316 (Orange)
- **Background:** #F0F9FF (Light Blue)
- **Text:** #0C4A6E (Dark)

### Tipografía
- **Font:** Plus Jakarta Sans (si está disponible en Typeform)
- **Alternativa:** San Francisco / -apple-system

### Logo
```
Mostrar logo en header (opcional)
O: Imagen de branding simples
```

---

## 🔗 BOTONES Y CTA

### Botón SIGUIENTE
```
Color: #F97316 (Orange)
Texto: "Siguiente →"
Cursor: pointer
```

### Botón SUBMIT
```
Color: #F97316 (Orange)
Texto: "Ver mi plan personalizado"
```

---

## 📧 INTEGRACIÓN POST-SUBMIT

En Typeform, después que el usuario envía:

### Opción A: Redirect a gracias
```
Settings → Responses → After submission
├─ Show thank you screen
├─ Mensaje: "¡Perfecto! Revisa tu email en 1 minuto"
└─ Redirect to: {landing-page}/gracias.html
```

### Opción B: Integración con email
Usa Zapier/Make para:
```
Typeform submit
    ↓
Guardar datos en Google Sheets/CRM
    ↓
Enviar email automático con plan personalizado
```

**Email de bienvenida debe incluir:**
- Nombre del usuario
- Su timeline calculado
- Cuántas ventas necesita/mes
- CTA a webinar/consulta

---

## 🔐 VARIABLES Y SCORING

Después del submit, Typeform captura:
```json
{
  "name": "valor",
  "city": "valor",
  "job": "valor",
  "monthly_income": 2100,
  "savings": 10000,
  "free_hours": 6,
  "time_slots": ["weekends"],
  "previous_business": "Sí, pero no funcionó",
  "timeline": "En 6 meses",
  "location_freedom": "Sí, eso sería increíble",
  "real_dream": "Viajar, estar con familia",
  "earning_potential": "Sí, suena increíble",
  "interest_level": "Sí, totalmente"
}
```

**Scoring automático (Zapier):**
```
HOT LEAD si:
  ├─ savings >= 5000
  ├─ free_hours >= 6
  ├─ timeline <= "En 6 meses"
  ├─ earning_potential IN ["Sí, suena increíble", "Sí, pero suena difícil"]
  └─ interest_level IN ["Sí, totalmente"]

Score > 4/5 = HOT → Email inmediato con oferta
Score 2-3/5 = WARM → Email educativo
Score <= 1/5 = COLD → Email de nurturing
```

---

## 🚀 PASOS DE IMPLEMENTACIÓN

1. **Copia la estructura anterior a Typeform**
   - Add questions one by one
   - Set required fields
   - Configure logic/branching (opcional)

2. **Personaliza colores**
   - Theme → Custom colors
   - Primary: #0EA5E9
   - Accent: #F97316

3. **Prueba el flujo**
   - Completa como usuario
   - Verifica que captura datos
   - Envía respuesta

4. **Configura webhook/integración**
   - Zapier: Trigger = Form submit
   - Action = Email + Google Sheets

5. **Obtén el URL**
   - Typeform dashboard
   - Share → Copylink
   - Ejemplo: https://inmomatch.typeform.com/to/aBcD1234

6. **Actualiza landing page**
   - Reemplaza alert() con window.open(typeformURL)
   - Testea en mobile y desktop

---

## 📊 DASHBOARD POST-LAUNCH

En Typeform puedes ver:
```
✓ Respuestas totales
✓ Completion rate (%)
✓ Tiempo promedio (min)
✓ Preguntas con mayor abandono
✓ Datos por respondente
```

Usa esto para optimizar:
- Si 40% abandona en Q7 → Simplifica esa pregunta
- Si Q11 tiene muchas respuestas vacías → Hazlo opcional
- Si Q12 tiene muchos "No, me parece mucho" → Ajusta messaging

---

## 🔗 TYPEFORM URL (Una vez creado)
```
Reemplaza esto en landing-page.html:
onclick="alert('Calculadora coming soon')"

CON esto:
onclick="window.open('https://inmomatch.typeform.com/to/YOUR_ID')"
```

---

*Typeform Setup | 2026-04-23*
