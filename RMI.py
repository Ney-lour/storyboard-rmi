import streamlit as st

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# ==========================================
st.set_page_config(
    page_title="Storyboard RMI - Desafíos de la Inclusión Neurodivergente",
    page_icon="🧠",
    layout="wide",
)

# Aplicar identidad visual basada en la paleta de colores de "Andes Multiplicado"
st.markdown(
    """
    <style>
    .main {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #0B3861; /* Azul principal */
    }
    .stAlert {
        background-color: #FFF3CD !important;
        color: #856404 !important;
        border-left: 5px solid #F5C242 !important; /* Amarillo acento */
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# BARRA LATERAL (MENÚ DE NAVEGACIÓN - NODOS)
# ==========================================
st.sidebar.title("🌲 Andes Multiplicado")
st.sidebar.subheader("Storyboard RMI Interactivo")
st.sidebar.markdown(
    "**Proyecto:** Desafíos de la inclusión neurodivergente en el entorno"
    " escolar"
)
st.sidebar.markdown("**Autores:** Jhon Díaz, Neybe Guerrero y Antonio Palacios")
st.sidebar.markdown("---")

nodo_seleccionado = st.sidebar.radio(
    "Seleccione el Nodo del Storyboard:",
    [
        "Nodo 0: Portada / Inicio",
        "Nodo 1: Mirada comparativa",
        "Nodo 2: Diana Garrido y La Casa del Viento",
        "Nodo 3: Salud ambiental y evidencia científica",
        "Nodo 4: Formación docente e inclusión educativa",
        "Nodo 5: Alimentación y convivencia escolar",
        "Nodo 6: Respuestas y participación",
    ],
)

# ==========================================
# CONTENIDO DE CADA NODO (ESTRUCTURA DEL STORYBOARD)
# ==========================================

if nodo_seleccionado == "Nodo 0: Portada / Inicio":
  st.title("Nodo 0: Portada / Inicio")
  st.markdown("### Planteamiento del problema y contexto de la neurodivergencia")

  col1, col2 = st.columns([2, 1])
  with col1:
    st.image(
        "https://images.unsplash.com/photo-1577896851231-70ef18881754?w=800&auto=format&fit=crop&q=60",
        caption="Entorno escolar y diversidad neurocognitiva",
        use_container_width=True,
    )
    st.write(
        "**Texto / Discurso base:** Presentación del problema central sobre"
        " las barreras institucionales, pedagógicas, alimentarias y"
        " socioambientales que afectan a los estudiantes neurodivergentes."
        " Introducción mediante un *vox populi* con testimonios breves de"
        " la comunidad."
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Banner interactivo con imagen y reproductor de audio (*vox populi*).\n-"
        " **Interactividad:** Botón de llamada a la acción para iniciar el"
        " recorrido por los nodos o saltar directamente al mapa."
    )

elif nodo_seleccionado == "Nodo 1: Mirada comparativa":
  st.title("Nodo 1: Mirada comparativa")
  st.markdown(
      "### Brechas de atención, leyes y realidades en Chile, Colombia y"
      " Venezuela"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.markdown(
        "**Análisis Comparativo y Normativo:**\n"
        "- **Venezuela:** Constitución (1999) y Ley Orgánica para la Inclusión,"
        " Igualdad y Desarrollo Integral de las Personas con Discapacidad"
        " (2024).\n"
        "- **Colombia:** Ley Estatutaria 1618 de 2013 y Decreto 1421 de 2017 sobre"
        " educación inclusiva.\n"
        "- **Chile:** Marcos normativos y brechas de atención en la infancia"
        " neurodivergente."
    )
    st.info(
        "🗺️ *(Visualización simulada de mapa interactivo geolocalizado con"
        " capas por país)*"
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Mapa geolocalizado interactivo.\n- **Interactividad:** Al hacer clic"
        " en cada país, se despliegan fichas legales y comparativas con enlaces"
        " a documentos oficiales."
    )

elif nodo_seleccionado == "Nodo 2: Diana Garrido y La Casa del Viento":
  st.title("Nodo 2: Diana Garrido y La Casa del Viento")
  st.markdown(
      "### Caso humano detonante sobre vivencias familiares, convivencia y"
      " barreras"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.image(
        "https://images.unsplash.com/photo-1544717305-2782549b5136?w=800&auto=format&fit=crop&q=60",
        caption="Entorno familiar y comunitario - La Casa del Viento",
        use_container_width=True,
    )
    st.write(
        "**Relato Periodístico:** Abordaje del caso de Diana Garrido y su"
        " experiencia familiar como conector empático y punto de partida para"
        " dimensionar las dificultades cotidianas que trascienden el aula"
        " hacia los espacios de convivencia y alimentación."
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Galería fotográfica documental y extractos de entrevista en audio con"
        " transcripción sincronizada.\n- **Interactividad:** Despliegue de"
        " citas destacadas mediante tarjetas interactivas."
    )

elif nodo_seleccionado == "Nodo 3: Salud ambiental y evidencia científica":
  st.title("Nodo 3: Salud ambiental y evidencia científica")
  st.markdown(
      "### Investigación explicativa sobre el eje intestino-cerebro y"
      " disruptores"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.markdown(
        "**Contenido Científico y Explicativo:**\n"
        "- Impacto de los disruptores endocrinos (EDCs), agroquímicos y"
        " derivados petroquímicos en la salud neurológica y física de los"
        " estudiantes.\n"
        "- Relación directa entre la contaminación cruzada alimentaria y el"
        " funcionamiento del eje intestino-cerebro."
    )
    st.warning("📊 *(Infografía Interactiva Científica con capas explicativas)*")
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Infografía interactiva explicativa basada en ciencia.\n- **Interactividad:"
        "** Botones desplegables para profundizar en cada factor químico y"
        " biológico sin saturar la lectura lineal."
    )

elif nodo_seleccionado == "Nodo 4: Formación docente e inclusión educativa":
  st.title("Nodo 4: Formación docente e inclusión educativa")
  st.markdown(
      "### Diagnóstico de planes de estudio universitarios y capacidades en el"
      " aula"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.write(
        "**Diagnóstico Pedagógico:**\n"
        "- Evaluación de los planes de estudio en las facultades de educación"
        " frente a las exigencias de la neurodiversidad.\n"
        "- Capacidades institucionales y carencias en la formación docente"
        " actual para ofrecer respuestas pedagógicas efectivas y ajustes"
        " razonables."
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Pódcast explicativo con testimonios de docentes y expertos en"
        " pedagogía inclusiva.\n- **Interactividad:** Reproductor de audio"
        " integrado con control de velocidad y transcripción desplegable."
    )

elif nodo_seleccionado == "Nodo 5: Alimentación y convivencia escolar":
  st.title("Nodo 5: Alimentación y convivencia escolar")
  st.markdown(
      "### Análisis de cantinas, protocolos alimentarios y la «tiranía de la"
      " lonchera aislada»"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.write(
        "**Enfoque Crítico y Social:**\n"
        "- Análisis de las cantinas escolares y los protocolos de alimentación."
        " La llamada 'tiranía de la lonchera aislada' como síntoma de la falta"
        " de corresponsabilidad institucional.\n"
        "- Necesidad de migrar del cuidado privado a políticas públicas de"
        " alimentación escolar inclusiva."
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Video corto documental y reportaje en texto enriquecido.\n-"
        " **Interactividad:** Enlaces contextuales cruzados hacia el Nodo 3"
        " (salud ambiental) y Nodo 2 (caso Diana Garrido)."
    )

elif nodo_seleccionado == "Nodo 6: Respuestas y participación":
  st.title("Nodo 6: Respuestas y participación")
  st.markdown(
      "### Sistematización de soluciones, buenas prácticas y recursos de"
      " consulta"
  )

  col1, col2 = st.columns([2, 1])
  with col1:
    st.write(
        "**Periodismo de Soluciones:**\n"
        "- Sistematización de buenas prácticas comunitarias, guías pedagógicas"
        " y recomendaciones de especialistas.\n"
        "- Espacio de participación ciudadana y recursos descargables de"
        " consulta para familias y docentes."
    )
  with col2:
    st.info(
        "📌 **Nota de Maquetación (Storyboard):**\n- **Recurso principal:**"
        " Video animado de soluciones e infografías descargables.\n-"
        " **Interactividad:** Formulario de comentarios y buzón de buenas"
        " prácticas ciudadanas."
    )

st.markdown("---")
st.markdown(
    "*Desarrollado para el proyecto **Desafíos de la inclusión neurodivergente"
    " en el entorno escolar** — Andes Multiplicado (2026).*"
)
