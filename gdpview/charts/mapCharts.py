from pyecharts.charts import Map
from pyecharts.options import LabelOpts, TitleOpts, VisualMapOpts

from gdpview.models import *


def fetch_data():
    province_data = GDPdata.objects.filter(year="2023").order_by("value")
    min_value = province_data.first().value
    max_value = province_data.last().value
    data_dict = []
    for _ in province_data:
        data_dict.append((_.region_name, _.value))
    m = Map()
    m.add(
        "GDP",
        data_dict,
        label_opts=LabelOpts(is_show=False),
        is_map_symbol_show=False

    ).set_global_opts(
        title_opts=TitleOpts(title="全国2023年各地区GDP"),
        visualmap_opts=VisualMapOpts(
            min_=min_value,
            max_=max_value
        ),
    )
    return m.render_embed()
