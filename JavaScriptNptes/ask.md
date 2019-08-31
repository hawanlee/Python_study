```
import React, {Component} from 'react';

export default class CalendarBuild extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentDay: '',
      currentMonth: '', 
      currentYear: '', 
      weekList: [
        {name: 'Mon', className: ''},
        {name: 'Tue', className: ''},
        {name: 'Wed', className: ''},
        {name: 'Thu', className: ''},
        {name: 'Fri', className: ''},
        {name: 'Sat', className: ''},
        {name: 'Sun', className: ''}
      ],
      dayList: [],
      def_month: this.props.def_month,
    }

    this.initCalendar = this.initCalendar.bind(this);
    this.renderHeader = this.renderHeader.bind(this);
    this.renderBody = this.renderBody.bind(this);
    this.preMonth = this.preMonth.bind(this);
    this.nextMonth = this.nextMonth.bind(this);
  }

  componentWillMount() {
    // style.use() // 需要配置loader 可以直接注释 忽略掉  实现每个模块卸载之后 css也会销毁 可以看之前写的一篇react css局部作用域的文章
  }

  componentWillUnmount() {
     // style.unuse() // 需要配置loader 可以直接注释 忽略掉 实现每个模块卸载之后 css也会销毁 可以看之前写的一篇react css局部作用域的文章
  }

  componentDidMount() {
    console.log(this.state.def_month);
    let tmp_date = new Date()
    tmp_date.setMonth(this.props.def_month)
    this.initCalendar(tmp_date)
  }

  componentWillReceiveProps(props){
    let tmp_date = new Date()
    tmp_date.setMonth(this.props.def_month)
    this.initCalendar(tmp_date)
    console.log(this.props.def_month);
    // this.preMonth()
    // this.forceUpdate()
  }

  // 获取当前date的当月第一天的字符串形式
  getMonthFirstDate(date) {
    let nowYear = date.getFullYear(); // 获取年份
    let nowMonth = date.getMonth()+1; // 获取月份
    return  `${nowYear}-${nowMonth}-01`
  }

  // 获取当前date的字符串形式
  getDateString(date) {
    let nowYear = date.getFullYear(); // 获取年份
    let nowMonth = date.getMonth()+1; // 获取月份
    let day = date.getDate();
    day = day < 10 ? '0' + day : day;
    return  `${nowYear}-${nowMonth}-${day}`
  }

  // 上个月
  preMonth(a) {
    let date = new Date(`${this.state.currentYear}-${this.state.currentMonth}-${this.state.currentDay}`)
    let preMonthFirstDate = new Date(this.getMonthFirstDate(new Date(date.setDate(0)))); // 0 是上个月最后一天
    this.initCalendar(preMonthFirstDate)
  }

  // 下个月
  nextMonth() {
    let date = new Date(`${this.state.currentYear}-${this.state.currentMonth}-${this.state.currentDay}`)
    let nextMonthFirstDate = new Date(this.getMonthFirstDate(new Date(date.setDate(33))));
    this.initCalendar(nextMonthFirstDate)
  }


  // 初始化日历
  initCalendar(currentDate) {
    // currentDate = new Date()
    // currentDate.setMonth(this.state.def_month)
    // console.log(this.state.def_month);
    let nowDate = currentDate ? currentDate : new Date();
    let nowMonthFirstDate = this.getMonthFirstDate(nowDate) // 获取当月1号日期，字符串格式：2010-01-01
    let nowWeek = new Date(nowMonthFirstDate).getDay() ? new Date(nowMonthFirstDate).getDay() : 7; // 获取星期
    let newDateList = []; // 创建日期数组
    let startDay =  2 - nowWeek; // 开始日期的下标  以为 setDate(0)是上个月最后一天  所以是2-nowWeek
    
    // let showDayLength = nowWeek < 6 ? 35 : 42;  // 如果5行能显示下一个月 就只显示5行
    let showDayLength = 35;  // 如果5行能显示下一个月 就只显示5行！只显示5行，避免对不齐

    // 循环处理 获取日历上应该显示的日期
    for (let i = startDay; i < startDay + showDayLength; i++) {
      let date = new Date(new Date(nowMonthFirstDate).setDate(i)); // 获取时间对象
      // let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate() // 小于9的数字前面加0
      let day = date.getDate() // 小于9的数字前面加0
      let dayObject = {
        date: this.getDateString(date),
        day,
        className: '',
      }
      // new Date(str).toDateString() === new Date().toDateString()
      if (date.toDateString() === new Date().toDateString()) {
        dayObject.className = 'today'
      }
      newDateList.push(dayObject)
    }

    let currentDay = nowDate.getDate()
    let currentMonth = nowDate.getMonth() + 1 >= 10 ? nowDate.getMonth() + 1 : '0' + (nowDate.getMonth() + 1)
    let currentYear = nowDate.getFullYear()
    
    this.setState(() => ({
        dayList: newDateList,
        currentDay: currentDay,
        currentMonth: currentMonth,
        currentYear: currentYear,
        // def_month: this.props.def_month,
      }))
  }

  renderHeader() {
    return(
      <div className = 'calendar-header'>
        {/* <div className = 'calendar-header-left'>
          <button onClick = {this.preMonth}>上个月</button>
        </div> */}
        <div className = 'cal_header_title'>
          {this.state.currentYear}.{this.state.currentMonth}
          <hr style={{width: '120px'}}/>
        </div>
        {/* <div className = 'calendar-header-right'>
          <button onClick = {this.nextMonth}>下个月</button>
        </div> */}
      </div>
    )
  }

  renderBody() {
    return(
      <div className = 'calendar-body'>
        <div className = 'week-container'>
          {this.state.weekList.map(week => {
            return <div key = {week.name} className = {`week ${week.className}`}>{week.name}</div>
          })}
        </div>
        <div className = 'day-container'>
          {this.state.dayList.map( (dayObject, index) => {
            return <div key = {index} className = {`day`}>
            {/* return <div key = {index} className = {`day ${dayObject.className}`}> */}
              <hr style={{width: '95%'}}/>
              {/* <h4>{dayObject.day}</h4> */}
              <h4>{dayObject.day}</h4>
              <div className='cal_events'>
              {/* <div><h4>{dayObject.day}</h4></div> */}
                <div>
                  <div className='events_auto_icons_EDR'></div>
                </div>
                {/* <div>
                  <div className='events_auto_icons_DRC'></div>
                </div>
                <div>
                  <div className='events_auto_icons_Clinic'></div>
                </div> */}
              </div>
              {/* <div style={{width: '100%', height: '15px' ,backgroundColor: '#00a0e9', lineHeight: '1em', marginBottom: '2px'}}>123</div>
              <div style={{width: '100%', height: '15px' ,backgroundColor: '#00a0e9', lineHeight: '1em', marginBottom: '2px'}}>123</div>
              <div style={{width: '100%', height: '15px' ,backgroundColor: '#00a0e9', lineHeight: '1em', marginBottom: '2px'}}>123</div>
              <div style={{width: '100%', height: '15px' ,backgroundColor: '#00a0e9', lineHeight: '1em', marginBottom: '2px'}}>123</div>
              <div style={{width: '100%', height: '15px' ,backgroundColor: '#00a0e9', lineHeight: '1em', marginBottom: '2px'}}>123</div> */}

            </div>
          })}
        </div>
      </div>
    )
  }

  render() {
    return(
      <div className = 'calendar'>
        {this.renderHeader()}
        {this.renderBody()}
      </div>
    )
  }
}

```