from pyecharts.charts import Map, Timeline, Pie, Grid, Bar, Line
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, TitleOpts, VisualMapOpts, GridOpts, InitOpts, LegendOpts, MarkPointOpts, \
    MarkPointItem, TooltipOpts, AxisOpts, AxisLineOpts, SplitLineOpts, AxisTickOpts
from pyecharts.types import VisualMap

from gdpview.models import GDPdata, NationalData


def fetch_data():
    national_data = NationalData.objects.all().order_by('year')
    x_data = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']  # x 轴的数据
    y_data = [_.value for _ in national_data.filter(type="国内生产总值")]
    y2_data = [_.value for _ in national_data.filter(type="人均国内生产总值")]
    y3_data = [_.value for _ in national_data.filter(type="国民总收入")]

    line = Line()  # 创建折线图实例
    line.set_global_opts(
        xaxis_opts=AxisOpts(type_="category"),  # 配置 x 轴类型为类别型
        yaxis_opts=AxisOpts(
            type_="value",
            axistick_opts=AxisTickOpts(is_show=True),
            splitline_opts=SplitLineOpts(is_show=True),
        ),
        legend_opts=LegendOpts(
            pos_left="5%",
            pos_top="55%"
        ),
        title_opts=TitleOpts(
            title="2014~2024年GDP、国民总收入变化情况",
            subtitle="数据来自国家统计局"
        )
    )
    line.add_xaxis(xaxis_data=x_data)  # 添加 x 轴数据
    line.add_yaxis(
        series_name="国内生产总值",  # 设置系列的名称
        y_axis=y_data,  # 添加 y 轴数据
        symbol="emptyCircle",  # 设置数据点的样式为空心圆
        is_symbol_show=True,
        label_opts=LabelOpts(is_show=False),
        is_smooth=True,
    ).add_yaxis(
        series_name="人均国内生产总值",
        y_axis=y2_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=LabelOpts(is_show=False),
        is_smooth=True
    ).add_yaxis(
        series_name="国民总收入",
        y_axis=y3_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=LabelOpts(is_show=False),
        is_smooth=True
    )
    timeline = Timeline(
        init_opts=InitOpts(
            width="1520px",
            height="800px",
            theme=ThemeType.WHITE,
        )
    )
    timeline.add_schema(
        orient="horizontal",
        is_auto_play=True,
        is_loop_play=True,
        is_timeline_show=True,
    )

    for year in range(2014, 2024):
        province_data = GDPdata.objects.filter(year=year).order_by("value")

        if not province_data.exists():
            continue

        min_value = province_data.first().value
        max_value = province_data.last().value

        data_dict = [(item.region_name, item.value) for item in province_data]

        bar = Bar(
            init_opts=InitOpts(
                width="200px",
                height="100px"
            ),
        )
        bar.add_xaxis([item.region_name for item in province_data])
        bar.add_yaxis("GDP", [item.value for item in province_data])
        bar.set_global_opts(
            legend_opts=LegendOpts(
                is_show=False
            ),
            visualmap_opts=VisualMapOpts(
                is_show=False
            )
        )

        pie = Pie(
            init_opts=InitOpts(
                width="600px",
                height="600px"
            )
        )
        pie.add(
            series_name=f"{year}年GDP分布",
            data_pair=data_dict,
            label_opts=LabelOpts(is_show=True),
            center=['85%', '25%'],
            radius='25%'
        ).set_global_opts(
            legend_opts=LegendOpts(is_show=False)
        )

        # Creating the Map chart
        map_chart = Map(
            init_opts=InitOpts(
                width="50%",
                height="80%"
            )
        )
        map_chart.add(
            series_name="GDP",
            data_pair=data_dict,
            label_opts=LabelOpts(is_show=False),
            is_map_symbol_show=False,
            layout_center=["50%", "40%"],
            layout_size="75%",
            is_roam=False
        ).set_global_opts(
            legend_opts=LegendOpts(is_show=False),
            title_opts=TitleOpts(
                title=f"全国{year}年各地区GDP",
                subtitle="不含港、澳、台数据",
                pos_left="40%"
            ),
            visualmap_opts=VisualMapOpts(
                min_=min_value,
                max_=max_value,
                is_show=False
            ),
        )

        grid = Grid(init_opts=InitOpts(width='100%', height='100%'))
        grid.add(line, grid_opts=GridOpts(pos_left="7%", pos_right="70%", pos_top="10%", pos_bottom="50%"))
        grid.add(bar, grid_opts=GridOpts(pos_left="10%", pos_bottom='10%', pos_top="70%"))
        grid.add(map_chart, grid_opts=GridOpts(pos_left="30%", pos_right="30%", pos_top="10%", pos_bottom="80%"))
        grid.add(pie, grid_opts=GridOpts(pos_right="0"))
        timeline.add(grid, time_point=str(year))
    return timeline.render_embed()
