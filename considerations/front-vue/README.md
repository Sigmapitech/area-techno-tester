# Consideration for Vue with Vue-Flow

## Overview
[Vue](https://vuejs.org/) is a progressive JavaScript framework for building user interfaces.
It is designed to be incrementally adoptable and can scale from a simple library to a full-featured framework.
[Vue Flow](https://vue-flow.dev/) is a Vue 3 component library for building node-based editors
and interactive graphs. It allows developers to create flow diagrams, node editors,
and other visual tools with ease.

## Why we considered it?
We considered Vue with Vue Flow because it provides a strong balance between simplicity,
flexibility, and visual interactivity. Our project requires workflows and visual
connections between elements, which Vue Flow can model directly inside a Vue app.Additionally,
by combining Vue with [CapacitorJS](https://capacitorjs.com/), we can package the project
as an Android app (and even iOS if needed). This allows us to reach mobile users without
rewriting the application.

## Who in the group has prior knowledge about this tech?
Yohann & Louis have prior experience in vue.js, making learning easier for the group.

## How could this tech allow us to improve our area workflow?
- Enable us to represent processes as interactive flow diagrams.
- Provide an intuitive UI for users to visualize and manipulate nodes, connections, and data.
- Enhance project presentations with dynamic, visual workflows instead of static diagrams.
- Improve collaboration by making workflows easier to understand.
- Extend the project to mobile platforms via CapacitorJS, making it available as an Android app.

## What is General feeling? (installation, tools, libs & support)
- **Installation**: Straightforward with npm. Vue Flow integrates seamlessly with Vue 3 projects.
- **Tools**: Works well with modern tooling like Vite.
- **Libraries & Support**: Vue Flow has clear documentation, examples. Vue itself has a
large ecosystem with long-term support.
- **Learning Curve**: Easy for simple projects but may require additional time for
customization of nodes and edges.

## Advantages
- Vue is lightweight, modular, and beginner-friendly.
- Vue Flow offers out-of-the-box features for drag-and-drop nodes, zooming, and edge handling.
- Strong ecosystem of Vue libraries for UI and state management.
- Reactive data binding makes updates to the flow seamless.
- Active community and good documentation.
- With CapacitorJS, the same Vue project can become a cross-platform app, including Android.

## Disadvantages
- Smaller ecosystem and fewer libraries compared to React.
- Vue's community, while active, is smaller than React's, leading to fewer resources
and third-party tools.
- Vue's flexibility can sometimes lead to inconsistent patterns across projects.
- CapacitorJS adds some complexity when configuring native builds.

## Use Cases
- Workflow automation tools.
- Process modeling apps.
- Educational tools for visual learning.
- Mind-mapping or brainstorming applications.
- Any project that benefits from visual node-based editing.

## Test
A web app containing a Vue Flow graph with nodes and connections.
Text, images, and buttons are displayed below the graph, demonstrating integration of
Vue Flow with standard Vue components.
The same project but packaged into an Android app.

## Conclusion
Vue with Vue Flow is a strong candidate for our project with the visual workflow and interactive graphs.
It provides a modern, reactive, and maintainable framework along with a specialized tool to
handle diagramming needs. While it introduces a slight learning curve, the advantages of interactivity,
flexibility, and clear visuals outweigh the drawbacks for our project context.
Furthermore, using CapacitorJS opens the door to delivering the same solution as a mobile app.
