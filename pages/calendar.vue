<template>
  <div>
    <v-container class="my-5">
      <v-simple-table>
        <template v-slot:default>
          <tbody>
            <tr v-for="(obj, key) in year" :key="key">
              <th width="4%" style="border: 1px solid grey">{{ key }}</th>
              <th width="4%" style="border: 1px solid grey" :style="obj.wareki.length > 1 ? 'background-color : #FFFF99' : ''">
                {{ obj.wareki.join(', ') }}
              </th>
              <template v-for="value in 12">
                <td width="3%" style="border: 1px solid grey">
                  <template v-if="obj.wareki.includes('承平5') && (value == 5 || value == 6)">
                    <nuxt-link :to="localePath({name : 'list', query : { year : '承平5', month : value }})">{{ value }}月</nuxt-link>
                  </template>
                  <template v-else>
                    {{value}}月
                  </template>
                </td>
                <td width="4%" style="border: 1px solid grey">
                  <span v-if="obj.uru == value">閏{{ value }}月</span>
                </td>
              </template>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  data() {
    return {
      baseUrl: process.env.BASE_URL,
    }
  },
  head() {
    const title = this.$t('honchoseiki')
    return {
      titleTemplate: null,
      title,
    }
  },
  methods: {},

  asyncData() {
    const fs = require('fs')
    const year = JSON.parse(fs.readFileSync('assets/json/year_jw.json'))
    return { year }
  },
}
</script>
