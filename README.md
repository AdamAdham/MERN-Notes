# React Notes

## Hooks

### 1. **`useState` Hook**  
#### Purpose:
- Manages state within a functional component.

#### Syntax:
```
const [state, setState] = useState(initialValue);
```

#### Key Points:
- **`state`**: The current state value.
- **`setState`**: Function used to update the state.
- **`initialValue`**: Can be a primitive, array, object, or any data type.

#### Example:
```
const [count, setCount] = useState(0);

return (
  <button onClick={() => setCount(count + 1)}>
    Clicked {count} times
  </button>
);
```

- **Optimization**: When setting state based on the previous state, use a function to access the previous state:
  ```
  setState(prevState => prevState + 1);
  ```

---

### 2. **`useEffect` Hook**  
#### Purpose:
- Handles side effects like data fetching, subscriptions, or manually manipulating the DOM.

#### Syntax:
```
useEffect(() => {
  // effect code here
  return () => {
    // cleanup code here
  };
}, [dependencies]);
```

#### Key Points:
- **No dependencies** (`[]`): Effect runs only once when the component mounts.
- **With dependencies** (`[dep1, dep2]`): Effect runs when one of the dependencies changes.
- **Return function**: Used for cleanup (e.g., unsubscribing from an event).

#### Example:
```
useEffect(() => {
  const fetchData = async () => {
    const result = await axios.get('/api/data');
    setData(result.data);
  };
  fetchData();
}, []); // Empty dependency array means it runs once on mount.
```

- **Optimization**: Make sure to list all dependencies in the array to avoid bugs.
- **Cleanup**: For example, cleaning up a subscription:
  ```
  useEffect (() => {
    window.addEventListener('resize', handleResize)
    return () => {
    window.removeEventListener('resize', handleResize)
  }
  ), [])
  ```

---

### 3. **`useContext` Hook**  
#### Purpose:
- Consumes a context created by `React.createContext` for sharing global state between components without props drilling.

#### Syntax:
```
const value = useContext(MyContext);
```

#### Key Points:
- **Context Provider**: Wraps around components that need access to the context.
- **useContext**: Extracts the value from the nearest `Context.Provider`.

#### Example:
```
const MyContext = React.createContext();

const MyComponent = () => {
  const value = useContext(MyContext);
  return <div>{value}</div>;
};

const App = () => (
  <MyContext.Provider value="Hello World">
    <MyComponent />
  </MyContext.Provider>
);
```

---

### 4. **`useReducer` Hook**  
#### Purpose:
- Manages complex state logic or when state transitions are based on actions, similar to Redux.

#### Syntax:
```
const [state, dispatch] = useReducer(reducer, initialState);
```

#### Key Points:
- **Reducer**: A function that takes `state` and `action` and returns the next state.
- **dispatch**: Function to trigger state transitions by passing actions.

#### Example:
```
const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </>
  );
};
```

- **When to use**: If you find `useState` becoming too cumbersome with complex logic or multiple variables.

---

### 5. **`useMemo` Hook**  
#### Purpose:
- Memoizes expensive calculations and returns a cached value until dependencies change. It prevents recalculations when not necessary, improving performance.

#### Syntax:
```
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

#### Key Points:
- **Dependencies**: If dependencies remain unchanged, the memoized value is reused.
- **Performance Optimization**: Useful in preventing expensive calculations from running on every render.

#### Example:
```
const computeExpensiveValue = (a, b) => {
  console.log('Calculating...');
  return a + b;
};

const MyComponent = ({ a, b }) => {
  const result = useMemo(() => computeExpensiveValue(a, b), [a, b]);

  return <div>{result}</div>;
};
```

- **Use sparingly**: Premature optimization can make code harder to maintain.

---

### 6. **`useCallback` Hook**  
#### Purpose:
- Returns a memoized version of a function, which is useful to prevent unnecessary re-renders when passing callbacks to child components.

#### Syntax:
```
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

#### Key Points:
- **When to use**: When passing a callback to child components that depend on props or state.
- **Prevents unnecessary re-renders**: The callback will only be recreated if dependencies change.

#### Example:
```
const MyComponent = ({ value }) => {
  const handleClick = useCallback(() => {
    console.log(value);
  }, [value]);

  return <button onClick={handleClick}>Click me</button>;
};
```

- **Similar to `useMemo`**: `useCallback` is used for functions, while `useMemo` is used for values.

---

### 7. **`useRef` Hook**  
#### Purpose:
- Stores a mutable object or DOM reference that persists across renders without causing re-renders.

#### Syntax:
```
const ref = useRef(initialValue);
```

#### Key Points:
- **Mutable object**: `ref.current` can be updated without re-rendering.
- **DOM manipulation**: Useful for accessing and manipulating DOM elements directly.

#### Example:
```JSX
const InputFocus = () => {
  const inputRef = useRef(null);

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus Input</button>
    </>
  );
};
```

- **Use case**: Storing a value that doesn’t cause re-renders (e.g., timer IDs, focus management).

---

### Differences

#### useMemo vs useCallBack
useMemo: Returns and stores the calculated value of a function in a variable
useCallBack: Returns and stores the actual function itself in a variable

