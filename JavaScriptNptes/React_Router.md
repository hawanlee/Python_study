# React Router

## 1. BrowserRouter
要使 React Router 正常工作，你需要将整个应用封装在 BrowserRouter 组件中
```
import { BrowserRouter } from 'react-router-dom';
...
ReactDOM.render(
  <BrowserRouter><App /></BrowserRouter>, document.getElementById('root')
  );
// 将整个应用封装在 BrowserRouter 组件中
```

## 2. Link
Link 是提供声明式、可访问的应用导航的简单方式。通过向 Link 组件传递 to 属性，可以告诉应用要路由到哪个部分。  
```
import { Link, Route } from 'react-router-dom'
...

<Link to='/review'>
    <h2 className='pro_timing'>TIMING</h2>
</Link>
```

## 3. Route
对于 Route 组件，如果你希望向 router 将渲染的特定组件传递属性，你需要使用 Route 的 render 属性。正如你所看到的，render使你能够控制渲染组件，进而使你能够向要渲染的组件传递任何属性。

总之，Route 组件是使用 React Router 构建应用的关键部分，因为该组件将根据当前的 URL 路径决定要渲染哪些组件。
```
<Route exact path='/review' render={()=>(
    <ReviewPage />)}>
</Route>
```