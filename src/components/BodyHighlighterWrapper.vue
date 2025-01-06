<template>
  <div ref="reactContainer"></div>
</template>

<script>
import { defineComponent, onMounted, onBeforeUnmount } from 'vue';
import React from 'react';
import ReactDOM from 'react-dom';
import BodyHighlighter from 'react-body-highlighter';

export default defineComponent({
  name: 'BodyHighlighterWrapper',
  props: {
    bodyType: {
      type: String,
      default: 'male', // 'male' or 'female' body type
    },
    highlights: {
      type: Array,
      default: () => [], // Array of muscle groups to highlight
    },
  },
  setup(props) {
    let reactRoot = null;

    onMounted(() => {
      // Create a new div container for the React component
      reactRoot = document.createElement('div');
      document.querySelector('[ref="reactContainer"]').appendChild(reactRoot);

      // Render the React component using React.createElement (no JSX)
      ReactDOM.render(
        React.createElement(BodyHighlighter, {
          bodyType: props.bodyType,
          highlights: props.highlights,
        }),
        reactRoot
      );
    });

    onBeforeUnmount(() => {
      // Clean up by unmounting the React component
      if (reactRoot) {
        ReactDOM.unmountComponentAtNode(reactRoot);
      }
    });
  },
});
</script>

<style scoped>
#reactContainer {
  width: 100%;
  max-width: 400px;
  margin: 20px auto;
}
</style>
