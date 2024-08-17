<script lang="ts" setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon/>
    </template>
    <template #heading>Timeseries Database</template>

    This project is a timeseries database that stores and retrieves data points. It is built with
    TimescaleDB, a PostgreSQL extension, and is designed to be scalable and efficient.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon/>
    </template>
    <template #heading>Graph Database</template>

    The project uses GraphDB, a graph database, to store and query data. It is designed to store RDF data and provide
    efficient querying capabilities.

    <br/>

    More instructions are available in <code>README.md</code>.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon/>
    </template>
    <template #heading>Python API</template>

    The project relòies on Python FastAPI framework to provide a RESTful API for interacting with the database.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon/>
    </template>
    <template #heading>Docker Deployment</template>

    The project is designed to be deployed using Docker containers.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon/>
    </template>
    <template #heading>Frontend</template>

    The project includes a frontend built with Vue.js and Vite. The frontend is designed to interact with the API and
    visualize data interactively
  </WelcomeItem>
</template>
