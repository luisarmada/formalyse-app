<template>
  <body>
    <div class="top-header-container">
      <h1>Activity</h1>
      <div class="day-streak-container">
        <div class="streak-counter">
          <span class="material-icons metrics-icon streak-flame">local_fire_department</span>
          <h2>120</h2>
        </div>
        <p>day streak</p>
      </div>
    </div>

    <div class="pr-display">
      <div class="pr-number-display">
        <span class="material-icons metrics-icon pr-medal">workspace_premium</span>
        <h2>105.5kg</h2>
      </div>
      <p>Most recent PR</p>
    </div>

    <SectionCategory class=""
      headerText="Your Charts" 
      redirect-text="Customise Graphs"
      redirectTo="/programs" 
    />

    <BarChart :chartType="currentChartType" :chartData="currentChartData" />

    <div class="chart-buttons">
      <button
        v-for="(chart, index) in charts"
        :key="index"
        @click="switchChart(chart)"
      >
        {{ chart.label }}
      </button>
    </div>

    <SectionCategory class=""
      headerText="Workout History" 
      redirect-text="View Calendar"
      redirectTo="/programs" 
    />

    <SectionCategory class=""
      headerText="Body Graph" 
      redirect-text="View Statistics"
      redirectTo="/programs" 
    />

    <BodyHighlighterWrapper :body-type="'male'" :highlights="['chest', 'biceps']" />
    
  </body>
  
</template>

<script>
import SectionCategory from '../components/SectionCategory.vue';
import BarChart from '../components/BarChart.vue';
import BodyHighlighterWrapper from '../components/BodyHighlighterWrapper.vue';


export default {
  name: 'ProgressPage',
  mounted() {
    // Enable navbar when this page is loaded
    this.$emit('toggleNavbar', true);
  },
  data() {
    return {
      currentChartType: 'bar',
      currentChartData: {
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        label: 'Workout Duration (mins)',
        data: [30, 45, 60, 40, 35, 50, 70],
      },
      charts: [
        {
          label: 'Workout Duration',
          type: 'bar',
          data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            label: 'Workout Duration (mins)',
            data: [30, 45, 60, 40, 35, 50, 70],
          },
        },
        {
          label: 'Volume',
          type: 'bar',
          data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            label: 'Workout Volume (kg)',
            data: [5000, 7000, 8500, 6000, 5500, 7500, 9000],
          },
        },
        {
          label: 'Weight Loss',
          type: 'line',
          data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7'],
            label: 'Weight (kg)',
            data: [90, 89.5, 89, 88.7, 88.2, 87.8, 87.5],
          },
        },
      ],
    };
  },
  components: {
    SectionCategory,
    BarChart,
    BodyHighlighterWrapper,
  },
  methods: {
    switchChart(chart) {
      this.currentChartType = chart.type;
      this.currentChartData = chart.data;
    },
  },
};
</script>

<style scoped>
  body{
    margin: 0px 18px;
  }

  .top-header-container{
    display: flex;
    flex-direction: row;
    width: 100%;
    margin-top: 24px;
    justify-content: space-between;
  }

  .day-streak-container{
    display: flex;
    flex-direction: column;
    gap: 0px;
    margin-top: 10px;
    margin-right: 8px;
    align-items: flex-end;
  }

  .streak-counter{
    display: flex;
    margin: 0;
  }

  .day-streak-container p{
    color: #bbb;
    margin: 0;
  }

  .day-streak-container h2{
    margin: 0;
  }

  .metrics-icon {
    display: inline-flex;
    align-items: center;
    height: 100%; /* Matches parent height */
    transform: translateY(-1px);
  }

  .streak-flame{
      color: #FFA500;
  }

  .pr-number-display{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 3px;
    margin: 0;
    height: auto;
  }

  .pr-number-display h2{
    margin: 0;
  }

  .pr-medal{
    color: #fedc56;
    transform: translateY(-1px);
    margin: 0;
  }

  .pr-display{
    display: flex;
    flex-direction: column;
    gap: 5px;
    width: auto;
    align-items: flex-start;
    margin: 24px 0px;
  }

  .pr-display p{
    color: #bbb;
    margin: 0;
    transform: translateX(3px);
  }

  .chart-buttons {
  display: flex;
  gap: 10px;
  margin: 20px 0;
  justify-content: center;
}

.chart-buttons button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  background-color: #008cba;
  color: white;
  cursor: pointer;
}

.chart-buttons button:hover {
  background-color: #005f75;
}

</style>