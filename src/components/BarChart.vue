<template>
    <div class="bar-chart-container">
      <canvas ref="barChartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);
  
  export default {
    name: 'BarChart',
    props: {
      chartType: {
        type: String,
        required: true,
      },
      chartData: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        chart: null,
      };
    },
    watch: {
      chartData: 'renderChart',
      chartType: 'renderChart',
    },
    mounted() {
      this.renderChart();
    },
    beforeDestroy() {
      if (this.chart) {
        this.chart.destroy();
      }
    },
    methods: {
      renderChart() {
        // Ensure the previous chart instance is destroyed
        if (this.chart) {
          this.chart.destroy();
          this.chart = null;
        }
  
        const ctx = this.$refs.barChartCanvas.getContext('2d');
        this.chart = new Chart(ctx, {
          type: this.chartType,
          data: {
            labels: this.chartData.labels,
            datasets: [
              {
                label: this.chartData.label,
                data: this.chartData.data,
                backgroundColor:
                  this.chartType === 'bar'
                    ? 'rgba(75, 192, 192, 0.5)'
                    : 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
                fill: this.chartType === 'line',
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: false, // Disable animation to prevent glitches
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      },
    },
  };
  </script>
  
  <style scoped>
  .bar-chart-container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
  }
  </style>
  