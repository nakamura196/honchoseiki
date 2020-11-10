<template>
  <div>
    <v-container class="my-5">
      <ul>
        <li v-for="(obj, index) in result" :key="index">
          {{index}}
          <ul>
            <li v-for="(obj2, index2) in obj" :key="index2">
              {{index2}}月
              <ul>
                <template v-for="(obj3, index3) in obj2" >
                <li :key="index3" v-if="index3 != 'undefined'">
                  
                  {{index3}}日
                  <ul>
                    <li v-for="(obj4, index4) in obj3" :key="index4">
                      <a :href="miradorUrl(obj4)" target="_blank">{{index4}}</a>
                    </li>
                    <li><a :href="miradorUrl2(obj3)" target="_blank">諸本を比較</a></li>
                  </ul>
                  
                </li>
                </template>
              </ul>
            </li>
          </ul>
        </li>
      </ul>

      
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
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
  methods: {
    miradorUrl(data){
      const params = [
        {
          manifest : data.manifest,
          canvas : data.canvas
        }
      ]
      return this.baseUrl + "/mirador/?params=" + encodeURIComponent(JSON.stringify(params))
    },
    miradorUrl2(data){
      const params = [
        
      ]
      for(let key in data){
        const obj = data[key]
        params.push({
          manifest : obj.manifest,
          canvas : obj.canvas
        })
      }
      
      return this.baseUrl + "/mirador/?params=" + encodeURIComponent(JSON.stringify(params))
    }
  },
  async asyncData() {
    const curation = await axios.get('https://mp.ex.nii.ac.jp/api/curation/json/858eb6c2-3b60-48a3-b152-9b1d35e01681').then((res) => {
      const curation = res.data
      const selections = curation.selections
      const result = {}
      for(let i = 0; i < selections.length; i++){
        const selection = selections[i]
        const members = selection.members
        for(let j = 0; j < members.length; j++){
          const member = members[j]
          const metadataObj = {}
          const metadata = member.metadata
          for(let k = 0; k < metadata.length; k++){
            const obj = metadata[k]
            metadataObj[obj.label] = obj.value
          }
          const year = metadataObj.year
          const month = metadataObj.month
          const day = metadataObj.day

          const label = member.label

          if(!result[year]){
            result[year] = {}
          }

          let tmp = result[year]
          if(!tmp[month]){
            tmp[month] = {}
          }

          tmp = tmp[month]

          if(!tmp[day]){
            tmp[day] = {}
          }

          tmp = tmp[day]

          tmp[label] = {
            manifest : selection.within["@id"],
            canvas : member["@id"]
           }
        }
      }
       return { result }
     })
    return curation
  },
}
</script>
