# AEC2: Fractals

## Chapter 1: Introduction

### Fractals as Visual Art

Since the beginning of time, humans have sought patterns in nature, attempting to understand its beauty and complexity. Fractals are one of those wonders that seem to merge science and art into a single entity. At first glance, fractals may appear to be simple abstract drawings, but behind their intricate patterns lie iterative mathematical formulas that produce infinite details, self-similar at any scale. The fascinating part is that these patterns are not only visually stunning but also present in our surroundings: from the branches of a tree to coastal formations and the structures of crystals.

This analysis aims to explore four specific types of fractals rendered in my program, *fract-ol*: Mandelbrot, Julia, Burning Ship, and Mandelbox, leveraging not only their mathematical richness but also their artistic potential. Additionally, I will examine how these fractals interact with fundamental principles of visual composition, such as Gestalt laws, the rule of thirds, and the use of color, bridging the gap between the abstract world of mathematics and the visual language we perceive as human beings.

### Brief Explanation of the Selected Fractals

### Mandelbrot: The Gateway to the Fractal World

The Mandelbrot fractal, often called "the fingerprint of God" by enthusiasts, is perhaps the most iconic of all. It is constructed from a simple mathematical formula:

Where zzz and ccc are complex numbers. The process involves iterating this formula to determine whether the values "escape" to infinity or remain bounded. The resulting visualization is a shape that resembles a "black heart" surrounded by infinite, symmetrical filigree, with details so minute that one can zoom in forever and continue discovering new patterns.

But Mandelbrot is not just a beautiful figure. It represents a way to explore the transitions between order and chaos. Every detail along its boundary holds complexity, patterns that appear repetitive but are never exactly the same. It’s like a miniature universe.

### Julia: The Infinite Family of Mandelbrot

Julia fractals can be thought of as the "children" of the Mandelbrot set. If we fix the value of ccc in the Mandelbrot formula and allow zzz to change, we obtain a Julia fractal. The interesting aspect is that depending on which value is chosen for ccc, the shapes can vary dramatically: some resemble connected networks (like a neural web), while others appear as separate fragments (like floating islands in an infinite sea).

Julia fractals invite experimentation. By playing with different values of ccc, one can transition from smooth, rounded structures to completely chaotic shapes. This dynamism makes them an excellent testing ground for analyzing how small variations in parameters can produce dramatically different visual results.

### Burning Ship

If Mandelbrot and Julia are fluid and smooth, Burning Ship is quite the opposite: jagged, angular, almost aggressive. This fractal uses a variant of the Mandelbrot set where the absolute values of the real and imaginary parts of the complex number are taken before squaring:

The result is a pattern that resembles a burning ship, with sharp edges and fractured structures. The difference in symmetry and texture makes it a visual representation that challenges traditional aesthetic rules, making it ideal for analyzing contrasts and the visual impact of color.

### Mandelbox: Exploring the Third Dimension

While the previous fractals are essentially two-dimensional, the Mandelbox takes things to the next level, generating three-dimensional structures. This fractal combines iterations and an escape formula based on a cube instead of a circle. What makes the Mandelbox special is its architecture: its forms resemble futuristic structures or even alien architectural designs.

Exploring the Mandelbox reveals how principles of three-dimensional composition, such as perspective and depth, play a crucial role in spatial perception. Additionally, it is fascinating how, despite being a purely mathematical construction, it seems to capture something intrinsically human—our fascination with order within chaos.

### Justification for the Selection

I chose to work with fractals not only because they are fascinating from a mathematical perspective but also because they represent a unique convergence of science, art, and technology. In a world where visuals dominate how we interact, fractals serve as a reminder that even in the seemingly abstract, there is beauty and meaning.

Moreover, fractals offer a unique opportunity to apply fundamental concepts of visual composition. Their self-similar patterns fit perfectly with Gestalt laws, while their infinite complexity challenges traditional rules of proportion and symmetry. In this project, I aim not only to analyze how fractals can be used to explore these ideas but also to demonstrate how, by adding interactivity and control over colors and parameters, something purely mathematical can be transformed into a visual and artistic experience.

## Chapter 2: Theoretical Foundations

### Fractals: Definition and Main Properties

A fractal is a geometric figure that can be divided into smaller parts, each of which is a scaled-down copy of the whole, known as self-similarity. Mathematically, fractals are objects defined by iterative formulas, where a simple pattern repeats at different scales. This phenomenon generates structures that appear infinitely complex and detailed, even when the base formula is surprisingly simple.

### Continuity: Visual Flows That Connect the Image

Continuity refers to our tendency to follow smooth lines, curves, or visual trajectories, allowing our gaze to explore an image fluidly. In fractals, this principle is notably present:

- **Mandelbrot**: The spirals emerging from the central cardioid are a perfect example of continuity. These curves seem to extend seamlessly, guiding the viewer toward the edges or more detailed areas. For instance, in zoom-ins, the spirals appear infinite, and the eye naturally follows their paths to new regions.
- **Julia**: In Julia fractals, the undulating curves connect different regions of the pattern, creating a sense of continuous flow. The bifurcations in the spirals serve as points of interest that do not break continuity but rather add additional layers for visual exploration.
- **Burning Ship**: Although this fractal has more rigid and angular edges, its continuity manifests in the main diagonals. The lines that appear to "ascend" toward the outer edges guide the viewer’s gaze as if navigating through flames.
- **Mandelbox**: In its three-dimensional projection, continuity is observed in the transitions between cubes and spheres, where repeated patterns seem to flow in predictable directions. This is particularly evident when rotating or exploring the fractal from different angles.

### Similarity: Cohesion in Self-Similarity

Similarity implies that visually alike elements tend to be perceived as part of a whole. In fractals, natural self-similarity makes this law especially relevant:

- **Mandelbrot**: The Mandelbrot set is filled with mini-Mandelbrots, small clones of the main shape that appear at different scales. These repetitions not only reinforce the fractal’s cohesion but also create a familiar visual pattern that aids overall perception.
- **Julia**: Julia structures are self-similar fragments of Mandelbrot. Each Julia fractal has visual coherence derived from its repeated patterns, such as branches that sprout into spirals or filigree that appear as echoes of previous forms.
- **Burning Ship**: Although its patterns are more chaotic, the repeated angular edges create a sense of structure. Dense areas with repeated diagonal lines reinforce the perception of similarity.
- **Mandelbox**: In the Mandelbox, each block appears to be a scaled copy of the previous one. The cubic patterns and repeating spheres give the fractal an appearance of "connected modules," generating strong visual cohesion.

### Proximity: Natural Grouping of Elements

Proximity states that elements close to each other tend to be perceived as part of a group. In fractals, this influences how we interpret dense and sparse regions:

- **Mandelbrot:** The areas around the central cardioid are densely packed with details, making them appear as a cohesive "core." In contrast, the outer branches have fewer details, creating a sense of dispersion and vastness.
- **Julia:** In Julia fractals, bifurcations tend to cluster in compact areas, forming clear visual groupings. Less dense regions seem to act as "bridges" between these groups.
- **Burning Ship:** This fractal uses proximity to create visual tension: dense shapes in the center contrast with the more dispersed edges. The tightly packed blocks give a sense of weight and force, defining the "burning ship."
- **Mandelbox:** In its three-dimensional projection, grouped blocks in certain areas appear as solid structures, while empty spaces create contrast and depth. This proximity in the design reinforces the perception of complex patterns.

### Figure and Background: Dynamic Contrast

The figure-ground law explains how we distinguish visual focal points (figure) from the background. Fractals play with this law in unique ways, shifting roles depending on zoom level or perspective:

- **Mandelbrot:** Initially, the black central cardioid is the dominant figure, while the colored edges form the background. However, as we zoom in, the details in the colored edges become new figures, transforming the visual context.
- **Julia:** The inner shapes of Julia fractals are usually well-defined figures, while the less dense outer zones are perceived as the background. This contrast is especially evident at the fractal's edges, where vivid colors stand out against darker tones.
- **Burning Ship:** The central "ship," with its angular structure and bright colors, acts as the figure against the black background or smooth gradients. When zooming in, the sharp edges of the flames can become secondary figures.
- **Mandelbox:** In the Mandelbox, three-dimensionality enhances this law. Depending on the viewing angle, certain structures may stand out as figures, while others recede into the background, creating a rich and dynamic visual experience.

### Relevant Visual Principles

### Gestalt Laws

Gestalt laws are psychological principles that explain how we perceive patterns and structures in our environment. In fractals, these laws are particularly useful for understanding why we see them as coherent and aesthetically pleasing figures.

1. **Continuity:** Our eyes tend to follow smooth lines and curves. In fractals like Julia or Mandelbrot, the continuous edges and fluid transitions between differently colored areas guide the eye through the image, creating an immersive visual experience.
2. **Similarity:** The self-similar patterns in fractals reinforce the perception of unity and order. Although each iteration adds unique details, repetitions create a sense of visual cohesion.
3. **Proximity:** Elements that are close together tend to be perceived as a group. In fractals like Mandelbox, three-dimensional shapes seem to connect and form complex structures because they are organized in closely packed blocks.
4. **Figure and Background:** Fractals often play with the perception of what is the figure and what is the background. For example, in Mandelbrot, the black center (the figure) strongly contrasts with the colored edges, but upon zooming in, the edge details can become new figures.

### Rule of Thirds

The rule of thirds is a basic visual composition principle that divides an image into nine equal parts with two horizontal and two vertical imaginary lines. The intersections of these lines are considered natural focal points for the human eye.

In fractals, although the shapes are mathematically generated and not consciously following these rules, it is possible to find visually significant areas that align with this proportion. For example:

- In Mandelbrot, the central "cardioid" often occupies a point near one of these intersections.
- When zooming in, new points of interest that emerge tend to intuitively fall in areas that follow this rule.

Incorporating this rule into the program’s design can help users frame more aesthetically balanced views, even within the chaotic nature of fractals.

### Golden Ratio

The golden ratio, represented by the number **ϕ = 1.618**, is known for its presence in natural structures and classical art as an aesthetically ideal proportion. This principle can be observed indirectly in fractals:

- In Mandelbrot, some of the patterns generated along the cardioid’s edges exhibit proportions close to the golden ratio, especially in the spiraling arms extending outward.
- In three-dimensional fractals like Mandelbox, the relationship between the dimensions of internal structures can align with this proportion, generating a sense of visual harmony.

Although fractals are not explicitly designed to follow these proportions, human perception tends to find harmonious relationships in them due to their self-similar complexity.

### Use of Color

Color plays a crucial role in fractal representation, translating abstract mathematical values into tangible visual experiences. Decisions about color palettes significantly affect how patterns and details are perceived.

1. **Color Psychology:**
    - **Blues and greens:** Convey calmness and serenity. In fractals like Mandelbrot, these palettes can highlight the smoothness of forms.
    - **Reds and oranges:** Generate energy and excitement. In fractals like Burning Ship, warm colors intensify the aggressiveness of the sharp edges.
    - **Dark gradients:** Can evoke mystery and depth, especially in three-dimensional fractals.
2. **Visual Impact:** Changing the color palette can completely alter the perception of a fractal. The same structure can appear chaotic with bright, warm colors or harmonious with soft, cool tones. This allows users to adapt the visual experience to their preferences or artistic intentions.
3. **Coloring Techniques:** Fractals are colored based on the number of iterations needed for a point to escape to infinity. This creates gradients and visual patterns that highlight the underlying structure. Palettes like linear spectrums, heat maps, or custom combinations add visual richness.

---

## Chapter 3: Program Implementation

This section describes the technical implementation of the program for generating and exploring fractals, explaining key aspects of design, interactivity, and added innovations.

### Programming Language and Libraries Used

The program is developed in **C**, a language that has been an essential part of my academic journey as a software engineering student. For graphical representation and user interaction, it uses the **MiniLibX (mlx) library**, a graphics library provided by **42 School**, designed for creating games and graphical applications. It offers basic functions for creating windows, drawing pixels, and handling keyboard and mouse events.

Additionally, the program utilizes the custom **libft** library (my first project at the academy), which includes auxiliary functions for string manipulation, memory management, and mathematical calculations.

### Main Functions

The program is structured around several key functions for generating and exploring fractals:

1. **Fractal Generation**
    - `draw_mandelbrot`: Calculates and draws the Mandelbrot set.
    - `draw_julia`: Renders Julia fractals, adjustable via interactive parameters.
    - `draw_burning_ship`: Generates the Burning Ship fractal with its distinctive angular features.
    - `draw_mandelbox`: Computes the Mandelbox with three-dimensional transformations projected onto 2D.

These functions iteratively calculate the evolution of complex points within the plane, using specific mathematical formulas for each fractal.

1. **Iteration Calculation**
    - `calc_bright`: Determines the number of iterations needed for a point to escape the set, directly influencing pixel brightness and color.
    - `map` and `calculate_ratio`: Scale screen coordinates to the complex plane, allowing fractals to be displayed at any resolution and enabling precise zooming.
2. **Graphical Representation**
    - `ft_put_pixel`: Colors specific pixels in the image buffer.
    - `iterate_screen`: Splits the screen into lines or regions, distributing work across multiple threads to optimize rendering.

### Interactivity

The program is designed to be highly interactive, allowing users to explore different views and customize the visualization experience:

1. **Zoom and Navigation**
    - Users can zoom into or out of specific fractal areas using the mouse (via the `mouse_hook` function) and navigate the complex plane with arrow keys.
    - This is controlled by adjusting the `zoom`, `x`, and `y` properties of the `t_position` structure.
2. **Formula Variations**
    - For Julia fractals, users can dynamically modify the complex parameter (`C`) using keyboard input, generating infinite variations within the Julia family.
3. **Color Palette Modification**
    - Users can switch between different color schemes by pressing specific keys. The palette directly affects how colors are assigned to iterations, highlighting unique patterns and details.

## Chapter 4: Visual Analysis of Fractals

### Mandelbrot Fractal

The Mandelbrot fractal is one of the most recognized due to its combination of infinite complexity and self-similarity, making it a visually fascinating object.

1. **General Composition and Zoom-In Details**
    - The main structure of the Mandelbrot set has a "heart" or "insect" shape, with outer regions revealing increasingly intricate patterns as one zooms in.
    - Details emerge at different scales with self-similar repetitions, reinforcing the **law of similarity**: each zoom level appears as a reflection of larger structures.
    - **Continuity** is evident in the smooth transitions between high- and low-density iteration zones, naturally guiding the viewer’s eye toward more complex areas.
2. **Gestalt Laws**
    - **Figure and Ground**: The black central shape contrasts sharply with the colored edges. When zooming in, the details at the edges become new figures, altering our initial perception.
    - **Proximity**: In the outer zones, dense patterns seem to form organized clusters. Nearby structures create the impression of being part of a cohesive whole.

### Julia Fractal

The Julia fractal, derived from formulas similar to Mandelbrot, offers a visual variety that depends entirely on initial parameters, making it ideal for artistic experimentation.

1. **Comparison with Mandelbrot**
    - While the Mandelbrot set represents a map of possible sets, the Julia fractal is a specific projection of those parameters.
    - Changing the **C** values generates radically different shapes, ranging from delicate filigrees to more compact structures.
2. **Aesthetic Aspects and Color Palette**
    - Julia’s shapes tend to be more symmetrical and balanced, highlighting the **law of continuity**. The fluid curves connect different parts of the fractal, guiding the viewer’s eye.
    - Warm color palettes, such as reds and yellows, can convey dynamism and energy, while cool tones, like blues and greens, enhance a sense of serenity and depth.

### Burning Ship

The Burning Ship fractal is less known, but its appearance is radically different due to its angular structure and sharp edges.

1. **Differences in Symmetry and Sharp Edges**
    - Unlike Mandelbrot and Julia, which have smooth curves, Burning Ship uses iterations based on absolute values, generating pointed edges and more chaotic structures.
    - This lack of smoothness slightly disrupts the **law of continuity**, but the clustering of details still adheres to the **law of proximity**.
2. **Visual Impact of Color Contrast**
    - The contrast between dark and bright tones at the edges highlights its abrupt and wild nature. Palettes that emphasize the angular edges (such as black and white or combinations of deep red and black) enhance the visual drama.

### Mandelbox

The Mandelbox introduces an additional dimension to the analysis as a three-dimensional fractal projected in 2D, adding a layer of perceptual complexity.

1. **Use of Three-Dimensionality**
    - The perception of depth and volume in the Mandelbox is achieved through color gradients and shadows calculated from iterations. This effect enhances **continuity**, as the eye can follow the "faces" of the Mandelbox as if exploring a solid object.
    - The internal structures of the Mandelbox exhibit **self-similar proportions**, making it ideal for identifying patterns related to similarity.
2. **Relation to the Golden Ratio**
    - Some of the internal subdivisions of the Mandelbox appear to naturally align with proportions close to the **golden section**. This occurs because fractal transformations tend to divide and reorganize space in a balanced way, generating a subconscious visual appeal.