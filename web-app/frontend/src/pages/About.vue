<template>
  <div class="about">
    <h1 class="about_title">
      О нас и нашей работе
    </h1>
    <div class="about_text">
      Я разобрал свою первую МКПП в 1995 году. Когда начало получаться, начали
      обращаться знакомые и соседи - так постепенно ремонт КПП и стал делом моей
      жизни. За 20 лет работы мы получили бесценный опыт и собрали огромный
      склад запчастей и гарантийных КПП, для того чтобы легко брать на себя
      любые, даже самые смелые, обязательства.<br />
      пециализированный сервисный центр KPPcentr.by обслуживает частный и
      коммерческий транспорт со всей республики и ближнего зарубежья. На
      сегодня, мы одни из лучших в Беларуси по ремонту и продаже МКПП. <br />
      Я отвечаю за все, что мы делаем, и подпишусь под каждым своим словом.
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.about {
  width: 100%;
  background-size: contain;
  height: 750px;
  background-image: url(../static/about.jpg);
}
.about_title {
  font-family: PlayfairDisplay-Bold;
  font-size: 70px;
  color: black;
  padding-top: 135px;
  text-align: center;
}

.about_text {
  text-align: center;
  padding-top: 57px;
  line-height: 24px;
  font-size: 25px;
  font-family: ProximaNovaRegular;
  font-weight: bold;
  color: #56534c;
  letter-spacing: 1px;
}
</style>
