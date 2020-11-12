<template>
  <div>
    <v-container class="my-5">
      <p>[凡例] 諸本の略解説</p>

      <ul>
        <li v-for="(obj, index) in result3" :key="index">
          {{index}}年
          <ul>
            <template v-for="(obj2, index2) in obj">
              <li class="my-2" :key="index2">
                {{index2}}月 [新訂増補国史体系1頁]
                <ul>
                  <template v-for="(obj3, index3) in obj2" >
                  <li class="my-2" :key="index3" v-if="index3 != 'undefined'">
                    
                    {{index3}}日 [1頁]
                    <ul>
                      <li class="my-2" v-for="(obj5, index5) in list" :keu="index5">
                        <template v-if="obj3[obj5]">
                          <a :href="miradorUrl(obj3[obj5])" target="_blank">{{obj5}}</a>
                        </template>
                        <template v-else>
                          {{obj5}}
                        </template>
                      </li>
                      <!--
                      <li v-for="(obj4, index4) in obj3" :key="index4">
                        <a :href="miradorUrl(obj4)" target="_blank">{{index4}}</a>
                      </li>
                      -->
                      <li class="my-2"><a :href="miradorUrl2(obj3)" target="_blank">諸本を比較</a></li>
                      <li class="my-2"> -> <a target="_blank">大日本史料（綱文検索）</a></li>
                    </ul>
                    
                  </li>
                  </template>
                </ul>
              </li>
            </template>
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
      list: ["宮内庁書陵部所蔵伏見宮本[伏417 第1巻] (伏417-1)", "駒場図・一高本", "京都御所東山御文庫本（画像は閲覧室のみ）", "宮内庁書陵部柳原本（柳-559） [第1冊]", "参考：旧・国史大系"],
      query: this.$route.query,
      result3 : {}
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
  mounted() {
    const result = this.result
    const query = this.query
    const result2 = {}

    for(let year in result){
      if(query.year && query.year != year){
        continue
      }

      const obj = result[year]
      const obj2 = {}

      for(let month in obj){
        if(query.month && query.month + '' != month + ''){
          continue
        }

        obj2[month] = obj[month]
      }

      result2[year] = obj2
    }
    
    this.result3 = result2
  },
  computed: {
    result2: function(){
      const result = this.result
      const query = this.query
      const result2 = {}

      for(let year in result){
        if(query.year && query.year != year){
          continue
        }

        const obj = result[year]
        const obj2 = {}

        for(let month in obj){
          if(query.month && query.month + '' != month + ''){
            continue
          }

          obj2[month] = obj[month]
        }

        result2[year] = obj2
      }
      
      return result2
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
