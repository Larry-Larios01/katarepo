1. whats a script type?
i think: is a the actual form to declare components
teh real meaning:in Vue.js, script type refers to the <script> block in Single File Components (SFCs). The type attribute can specify how the script is processed, such as type="module" for ES modules or other preprocessors like TypeScript (type="ts"). Typically, the script block is used to define the logic, including imports, data, methods, and other options of the component.


2. whats define component?
i think: is older than script type and yo can declare components yo need to put the props and another things in there
the real meaning: defineComponent is a helper function provided by Vue 3, primarily used with TypeScript to define components with proper type inference and IntelliSense support. It helps structure components in a modular and typed way, allowing better integration with advanced tools like TypeScript.


3. which is better?
i think: is think they have a god thinks script type is less verbose than defien component but define component you can organize it first you need
the real meaning:his is subjective and depends on use cases. script setup is a newer syntax introduced in Vue 3.2, offering simplicity and less boilerplate, making it ideal for most scenarios. defineComponent is better suited for more complex setups, especially when using TypeScript, as it offers explicit type declarations and a more traditional structure.

4. whats rfc?
i thing: is request for comments and is the way of vue js request to teh users to the new functionalities and tehy decide if they put it on framework
the the real menaing is: RFC stands for "Request for Comments," a process used by the Vue.js team (and other open-source communities) to propose new features, changes, or updates to the framework. It provides a formal way for the community to discuss and refine ideas before they are implemented.


5. whats DOM?
i think: idk
tehreal meaning: In Vue.js, the DOM (Document Object Model) refers to the structured representation of your HTML document. Vue interacts with the DOM dynamically to render components, update the UI, and respond to user interactions. Vue uses its reactivity system and a virtual DOM to optimize updates to the real DOM.


6. what is reactive?
i think: is when an atributte can change
the real meaning: In Vue.js, reactive refers to a method that makes an object reactive, enabling it to track changes to its properties and automatically update the DOM or dependent computations.

7. whats sfc?
i think: is when you put all the html, css etc in a one file
teh real meaning: SFC (Single File Component) is a Vue.js file structure that includes the template, script, and styles of a component within a single .vue file, keeping everything modular and organized.


8. whats computer property?
ithink: idk
teh real meaning: In Vue.js, a computed property is a feature that allows you to define properties that are derived from other reactive data. These properties are automatically recalculated when their dependencies change and are cached until those dependencies change again.

Computed properties are particularly useful when you need to perform complex calculations or transformations on your data and want to keep your templates clean.

9. how v-show works?
i think: idk 
the real meaning:v-show conditionally displays elements in Vue.js by toggling the display CSS property. Unlike v-if, it doesn't remove the element from the DOM, improving performance for frequent toggling.


10. whats inline detection: 
i think: is when we check each line by each line if something happend
the real meaning:This is not a Vue.js-specific term. If referring to Vue, it might relate to in-line error detection or logging for debugging directly in the code.



11. whats a hook? 
i think: idk
the real menaing is: In Vue.js, a hook refers to lifecycle hooks—special functions or methods that allow you to run code at specific stages of a component's lifecycle. These hooks provide developers with control over what happens when a component is created, mounted, updated, or destroyed.


12. whats is a call back?
i think: idk
the real meaning:A callback is a function that is passed as an argument to another function and is intended to be executed later, either synchronously or asynchronously. Callbacks are a fundamental concept in programming, especially in JavaScript, for managing tasks like event handling, asynchronous operations, or custom logic within functions.


13. whats a component?
i think: is a set of html, css and  js that you can import 
the real meaning:In Vue.js, a component is a reusable block of HTML, CSS, and JavaScript that encapsulates logic and presentation. It’s the building block for creating modular and maintainable applications.



14. whats a props?
i think is: a properties?
the real meaning: In Vue.js, props are a mechanism for passing data from a parent component to a child component. They allow a parent component to configure or customize the behavior of a child component by providing values.


15. how slot works? 
i think:is replace what is in the template 
the real meaning: In Vue.js, slots are a mechanism that allows you to pass custom content into a component's template from its parent component. Slots are especially useful for creating reusable and flexible components where the parent can define part of the content.


16. how "is" works?
i think:
the real meaning: In the context of Vue.js, the :is attribute is a special attribute used with the <component> element to dynamically render a component. It allows you to specify which component to display dynamically, based on a reactive or computed value.

17. whats a event?
i think: when something specific happend
the real meaning: In Vue.js, an event is a trigger or action that occurs as a result of user interaction or programmatic changes, like clicks or data updates.

18.  how $emit works?
teh real menaing: $emit allows child components to send custom events to their parent components, enabling communication between components.



19. how that sintaxis works = <MyButton @increase-by="(n) => count += n" />?
i think: when you pass n the value of n pass to count?
the real meaning:This syntax binds the increase-by event emitted by MyButton to an inline handler (n) => count += n. When increase-by is emitted with a value n, it adds n to count.


20. whats fallthrough attr?
i think: is get all the attrs form inherency 
the real emaning:The fallthrough attribute in the context of Vue.js refers to a behavior where attributes not explicitly defined in a component are passed through to the root element of that component. These are sometimes called "inherited attributes."

21. whats hidrate in the context of vue?
i think: i have no idea
the real meaning

Hydrate on Idle in Vue.js (and in frontend frameworks in general) is an optimization technique where the process of hydration—linking Vue's reactivity system to pre-rendered server-side HTML—is deferred until the browser is idle. It uses APIs like requestIdleCallback to run the hydration process when the browser has completed other high-priority tasks, improving the initial load performance and user experience.  (The term idle means inactive, not in use, or waiting for a task to perform. In the context of computers, programming, and browsers, it refers to a state where the system or a resource (like the CPU or browser) is not actively engaged in high-priority tasks and is available for low-priority or background work.)

Hydrate on Visibility is another optimization strategy similar to Hydrate on Idle, but instead of waiting for the browser to be idle, the hydration process is delayed until the component or part of the page becomes visible in the viewport. This is often achieved using the Intersection Observer API or similar techniques.

Hydrate on Media Query is an optimization technique where hydration is conditionally performed based on specific media query criteria, such as screen size, resolution, or device type. This approach allows you to defer or prioritize hydration depending on the user's device or viewport characteristics.(A media query is a CSS feature used to apply styles conditionally based on specific characteristics of the user's device, such as screen size, resolution, orientation, or other media features. Media queries are essential for creating responsive web designs, ensuring a website looks and functions well on various devices, from mobile phones to desktop monitors.)


Hydrate on Interaction is an optimization technique where the hydration process (attaching client-side JavaScript to server-rendered HTML) is delayed until the user interacts with a specific element or area of the page. This technique improves the initial load performance by deferring non-critical JavaScript execution until it's genuinely needed.




21. whats render?
i think: is put all the reactive props in the html
the real meaning: Render refers to the process of generating and displaying content (typically HTML, CSS, and JavaScript) to the user on a webpage or application. In the context of web development, rendering can happen on the client side, the server side, or even on both. It is a key concept in frameworks like Vue.js, React, and others.